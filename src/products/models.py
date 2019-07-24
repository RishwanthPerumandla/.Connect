from django.db import models

# Create your models here.

CATEGORY_CHOICES = (
    ('Books','BOOKS'),
    ('Electronics', 'ELECTRONICS'),
    ('Fashion','FASHION'),
    ('Stationary','STATIONARY'),
    ('Others','OTHERS'),
)	

class Product(models.Model):
	product_id 	= models.AutoField
	title 		= models.CharField(max_length=60)
	category	= models.CharField(max_length=12,default='',choices=CATEGORY_CHOICES)
	description = models.CharField(blank=False, null=True, max_length=80)
	price 		= models.IntegerField(default=0)
	image 		= models.ImageField(blank=False,upload_to='items/images',default='')
	email 		= models.EmailField(blank=False,default='')		

	def __str__(self):
		return self.title


