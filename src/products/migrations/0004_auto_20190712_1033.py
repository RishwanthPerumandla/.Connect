# Generated by Django 2.0.7 on 2019-07-12 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20190712_1010'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='summary',
        ),
        migrations.AddField(
            model_name='product',
            name='email',
            field=models.EmailField(default='Your Email Id', max_length=254),
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(default='Your Name', max_length=120),
        ),
    ]
