from fcm_django.models import FCMDevice

from users.models import User
from django.db.models.query import QuerySet


def get_user_devices(user: User) -> QuerySet[FCMDevice]:
    """
    return all the user devices
    """
    return FCMDevice.objects.filter(user=user)


def get_or_create_user_device(
        user: User, registration_token: str
) -> FCMDevice:
    """
    return the last user devices
    """
    devices = get_user_devices(user)
    for device in devices:
        device.active = False
        device.save()
    user_device, created = FCMDevice.objects.get_or_create(
        user=user, registration_id=registration_token
    )
    user_device.active = True
    user_device.save()
    return user_device
