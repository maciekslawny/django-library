# Generated by Django 3.0.14 on 2021-07-15 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teczka', '0010_auto_20210715_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teczka',
            name='customs',
            field=models.BooleanField(blank=True),
        ),
        migrations.AlterField(
            model_name='teczka',
            name='invoice',
            field=models.BooleanField(blank=True),
        ),
        migrations.AlterField(
            model_name='teczka',
            name='vgm',
            field=models.BooleanField(blank=True),
        ),
    ]
