# Generated by Django 4.2.1 on 2023-06-05 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_produktas_delete_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produktas',
            name='kategorija',
            field=models.CharField(choices=[('M', 'Medziaga'), ('O', 'Oda'), ('U', 'Universalus'), ('SE', 'Sepeciai')], max_length=2),
        ),
    ]