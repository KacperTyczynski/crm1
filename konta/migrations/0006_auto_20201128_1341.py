# Generated by Django 3.1.3 on 2020-11-28 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('konta', '0005_auto_20201128_1330'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zamowienie',
            name='tags',
        ),
        migrations.AddField(
            model_name='produkt',
            name='tags',
            field=models.ManyToManyField(to='konta.Tags'),
        ),
    ]
