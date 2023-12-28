from decimal import Decimal

from cardb.models import Products


class Basket:
    """
    A base Basket class, providing some default behaviors that
    can be inherited or overridden, as necessary.
    """

    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('skey')
        if 'skey' not in request.session:
            basket = self.session['skey'] = {}
        self.basket = basket

    def add_product(self, product_id, quantity=1):
        """
        Add a product to the basket or update its quantity.
        """
        product_id = str(product_id)
        if product_id in self.basket:
            self.basket[product_id]['quantity'] += quantity
        else:
            # If the product is not in the basket, add it
            self.basket[product_id] = {'quantity': quantity}

        # Save the basket in the session
        self.save()

    def remove_product(self, product_id):
        """
        Remove a product from the basket.
        """
        product_id = str(product_id)
        if product_id in self.basket:
            del self.basket[product_id]

        # Save the basket in the session
        self.save()

    def remove_product_quantity(self, product_id, quantity=1):
        """
        Remove a specified quantity of a product from the basket.
        If the quantity becomes zero or less, remove the product from the basket entirely.
        """
        product_id = str(product_id)
        if product_id in self.basket:
            self.basket[product_id]['quantity'] -= quantity
            if self.basket[product_id]['quantity'] <= 0:
                del self.basket[product_id]

        # Save the basket in the session
        self.save()


    def get_basket_summary(self):
            """
            Get a summary of the products in the basket.
            """

            basket_summary = {}
            totalall=Decimal('0.00')
            for product_id, product_data in self.basket.items():
                total = Decimal('0.00')
                try:
                    product = Products.objects.get(id=int(product_id))
                    total += Decimal(product.price) * product_data['quantity']
                    totalall += total
                    basket_summary[product_id] = {
                        'name': product.name,
                        'price': str(product.price),
                        'quantity': product_data['quantity'],
                        'total':total,
                        # Add more details as needed
                    }
                except Products.DoesNotExist:
                    # Handle the case where the product is not found in the database
                    pass
            response_dataa = {
                'basket_summary': basket_summary,
                'total': str(totalall),  # Convert Decimal to string for serialization
            }

            return response_dataa

    def get_basket_total(self):
            """
            Calculate the total value of items in the basket.
            """
            total = Decimal('0.00')

            for product_id, product_data in self.basket.items():
                try:
                    product = Products.objects.get(id=int(product_id))
                    total += Decimal(product.price) * product_data['quantity']
                except Products.DoesNotExist:
                    # Handle the case where the product is not found in the database
                    pass

            return total

    def save(self):
        """
        Save the basket in the session.
        """
        self.session['skey'] = self.basket
        self.session.modified = True

    def clear_basket(self):
        """
        Clear all products from the basket.
        """
        self.basket = {}
        self.save()