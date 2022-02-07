# Generated by Django 4.0.1 on 2022-02-07 20:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('northwind', '0011_alter_product_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='northwind.customer'),
        ),
        migrations.AlterField(
            model_name='order',
            name='employee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='northwind.employee'),
        ),
    ]
