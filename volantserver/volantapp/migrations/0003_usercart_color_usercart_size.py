# Generated by Django 5.0 on 2024-09-10 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volantapp', '0002_cartitem_color_cartitem_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercart',
            name='color',
            field=models.ManyToManyField(through='volantapp.CartItem', to='volantapp.color'),
        ),
        migrations.AddField(
            model_name='usercart',
            name='size',
            field=models.ManyToManyField(through='volantapp.CartItem', to='volantapp.size'),
        ),
    ]
