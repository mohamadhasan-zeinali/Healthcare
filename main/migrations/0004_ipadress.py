# Generated by Django 4.0.4 on 2022-07-21 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_mainmodel_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='IPAdress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField(verbose_name='آیپی ها')),
            ],
        ),
    ]