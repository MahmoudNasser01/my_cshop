# Generated by Django 4.2.7 on 2023-11-21 12:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cardb', '0003_alter_products_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='sections',
            name='user',
            field=models.ForeignKey(default=1, limit_choices_to={'role': 'SELLER'}, on_delete=django.db.models.deletion.CASCADE, related_name='sections', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]