# Generated by Django 4.2.1 on 2023-06-10 13:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_payment_orderplaced'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='user',
        ),
        migrations.RenameField(
            model_name='cart',
            old_name='user',
            new_name='vartotojas',
        ),
        migrations.DeleteModel(
            name='OrderPlaced',
        ),
        migrations.DeleteModel(
            name='Payment',
        ),
    ]
