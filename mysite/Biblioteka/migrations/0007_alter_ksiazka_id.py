# Generated by Django 3.2.3 on 2021-06-05 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Biblioteka', '0006_alter_ksiazka_wypozyczajacy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ksiazka',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
