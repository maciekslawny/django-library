# Generated by Django 3.0.14 on 2021-07-17 17:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teczka', '0013_auto_20210717_1923'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teczka',
            old_name='destination',
            new_name='pod',
        ),
        migrations.AlterField(
            model_name='teczka',
            name='cut_off',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 7, 17, 19, 24, 25, 47769), null=True),
        ),
        migrations.AlterField(
            model_name='teczka',
            name='etd',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 7, 17, 19, 24, 25, 47769), null=True),
        ),
        migrations.AlterField(
            model_name='teczka',
            name='loading_data',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 7, 17, 19, 24, 25, 47769), null=True),
        ),
    ]