# Generated by Django 4.1.7 on 2023-03-10 00:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppECP', '0021_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carrito_item',
            name='carrito',
        ),
        migrations.RemoveField(
            model_name='carrito_item',
            name='producto',
        ),
        migrations.DeleteModel(
            name='Carrito',
        ),
        migrations.DeleteModel(
            name='Carrito_item',
        ),
    ]
