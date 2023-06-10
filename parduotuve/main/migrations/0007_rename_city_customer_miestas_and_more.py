# Generated by Django 4.2.1 on 2023-06-06 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_remove_customer_state'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='city',
            new_name='miestas',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='locality',
            new_name='pavarde',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='mobile',
            new_name='telefonas',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='name',
            new_name='vardas',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='user',
            new_name='vartotojas',
        ),
        migrations.AddField(
            model_name='customer',
            name='salis',
            field=models.CharField(choices=[('Lietuva', 'Lietuva'), ('Latvia', 'Latvia'), ('Estonia', 'Estonia')], default=6.6, max_length=100),
            preserve_default=False,
        ),
    ]
