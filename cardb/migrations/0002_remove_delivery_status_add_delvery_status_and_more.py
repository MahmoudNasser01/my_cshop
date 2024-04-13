# Generated by Django 4.2.7 on 2024-04-13 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cardb', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='delivery',
            name='status',
        ),
        migrations.AddField(
            model_name='add_delvery',
            name='status',
            field=models.CharField(choices=[('active', 'active'), ('pending', 'pending'), ('rejected', 'rejected'), ('completed', 'completed')], default='active', max_length=20),
        ),
        migrations.AddField(
            model_name='delivery',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
