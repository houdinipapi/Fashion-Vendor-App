# Generated by Django 5.0.1 on 2024-01-28 15:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("item", "0002_alter_category_options_item"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="item",
            options={"ordering": ("name",)},
        ),
        migrations.AlterField(
            model_name="item",
            name="price",
            field=models.FloatField(),
        ),
    ]
