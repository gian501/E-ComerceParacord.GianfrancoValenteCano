# Generated by Django 4.1.7 on 2023-03-07 20:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppECP', '0012_alter_producto_image_alter_profile_image_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
