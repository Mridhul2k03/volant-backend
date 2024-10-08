# Generated by Django 5.0 on 2024-09-10 04:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volantapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='color',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='volantapp.color'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cartitem',
            name='size',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='volantapp.size'),
            preserve_default=False,
        ),
    ]
