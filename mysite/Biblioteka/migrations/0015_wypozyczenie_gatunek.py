# Generated by Django 3.2.3 on 2021-06-08 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Biblioteka', '0014_alter_wypozyczenie_tytul'),
    ]

    operations = [
        migrations.AddField(
            model_name='wypozyczenie',
            name='gatunek',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
