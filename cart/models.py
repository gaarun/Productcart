from django.db import models
from  django.conf import settings
from store.models import Products
User = settings.AUTH_USER_MODEL
# Create your models here.
class Cart(models.Model):
	user		=	models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
	product		=	models.ManyToManyField(Products,blank=True)
	total		=	models.DecimalField(default=0.00,max_digits=100,decimal_places=2)
	updated		=	models.DateTimeField(auto_now=True)
	timestamp	=	models.DateTimeField(auto_now=True)

	def __str__(self):
		return str(self.id)
