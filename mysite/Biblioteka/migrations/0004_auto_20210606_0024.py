# Generated by Django 3.2.3 on 2021-06-05 22:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Biblioteka', '0003_ksiazka_wypozyczajacy'),
    ]

    operations = [
        migrations.AddField(
            model_name='ksiazka',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='ksiazka',
            name='wypozyczajacy',
            field=models.CharField(blank=True, default='', max_length=13),
        ),
    ]
