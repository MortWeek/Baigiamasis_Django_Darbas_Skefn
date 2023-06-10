# Generated by Django 4.2.1 on 2023-06-05 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produktas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pavadinimas', models.CharField(max_length=100)),
                ('kaina', models.FloatField()),
                ('kaina_su_nuolaida', models.FloatField()),
                ('aprasymas', models.TextField()),
                ('composition', models.TextField(default='')),
                ('prodapp', models.TextField(default='')),
                ('kategorija', models.CharField(choices=[('M', 'Medziaga'), ('O', 'Oda'), ('U', 'Universalus'), ('MS', 'Milkshake'), ('PN', 'Paneer'), ('GH', 'Ghee'), ('CZ', 'Cheese'), ('IC', 'Ice-Creams')], max_length=2)),
                ('nuotrauka', models.ImageField(upload_to='product')),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]