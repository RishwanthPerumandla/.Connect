# Generated by Django 2.1.7 on 2019-07-17 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_auto_20190717_1111'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productimage',
            name='image',
        ),
        migrations.RemoveField(
            model_name='productimage',
            name='products',
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='items/images/download.png', upload_to='items/images'),
        ),
        migrations.DeleteModel(
            name='ProductImage',
        ),
        migrations.DeleteModel(
            name='RelatedImage',
        ),
    ]
