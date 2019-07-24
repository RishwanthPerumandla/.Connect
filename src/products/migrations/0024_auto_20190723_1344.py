# Generated by Django 2.1.7 on 2019-07-23 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0023_auto_20190723_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Books', 'BOOKS'), ('Electronics', 'ELECTRONICS'), ('Fashion', 'FASHION'), ('Stationary', 'STATIONARY'), ('Others', 'OTHERS')], default='', max_length=12),
        ),
    ]