# Generated by Django 2.0.3 on 2018-03-29 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20180329_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcategory',
            name='root',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.ProductCategory'),
        ),
    ]
