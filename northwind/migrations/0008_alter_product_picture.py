# Generated by Django 4.0.1 on 2022-02-04 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('northwind', '0007_alter_product_picture_alter_product_supplier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='upload_dir'),
        ),
    ]