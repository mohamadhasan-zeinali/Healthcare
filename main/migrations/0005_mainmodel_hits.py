# Generated by Django 4.0.4 on 2022-07-21 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_ipadress'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainmodel',
            name='hits',
            field=models.ManyToManyField(blank=True, related_name='hits', to='main.ipadress', verbose_name='بازدید ها'),
        ),
    ]