# Generated by Django 4.2.6 on 2023-10-17 16:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("aboutCompany", "0004_alter_location_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="location",
            name="address",
            field=models.TextField(verbose_name="Адрес кафе"),
        ),
        migrations.AlterField(
            model_name="location",
            name="name",
            field=models.CharField(max_length=30, verbose_name="Название кафе"),
        ),
        migrations.AlterField(
            model_name="location",
            name="photo",
            field=models.FileField(upload_to="", verbose_name="Фотография"),
        ),
    ]
