from django.db import models
from django import forms
import datetime
#Create Choices here
gender	=	(('M','Male'),
			('F','Female'),
			('O','Others'),
			)

# Create your models here.
class ProductType(models.Model):
	product_type		=	models.CharField(max_length = 20)

	def __str__(self):
		return self.product_type

#Creare your ProductManager here.
class ProductManager(models.Manager):
	#product Name filter
	def product_name_startswith(self,name):
		return super(ProductManager,self).get_queryset().filter(product_name__startswith=name)
	def product_name_endswith(self):
		return super(ProductManager,self).get_queryset().filter(product_name__iendswith="s")
	def product_name_fullmatch(self):
		return super(ProductManager,self).get_queryset().filter(product_name__iexact="s")
	def product_name_contains(self):
		return super(ProductManager,self).get_queryset().filter(product_name__icontains="s")
	
	#Products type filter here.
	def product_type_startswith(self):
		return super(ProductManager,self).get_queryset().filter(product_type__product_type__startswith="electronic")
	def product_type_endswith(self):
		return super(ProductManager,self).get_queryset().filter(product_type__product_type__endswith="s")
	def product_type_fullmatch(self,name):
		return super(ProductManager,self).get_queryset().filter(product_type__product_type__contains=name)
	def product_type_contains(self):
		return super(ProductManager,self).get_queryset().filter(product_type__product_type__icontains="s")

	#Products desc filter here.
	def product_desc_startswith(self):
		return super(ProductManager,self).get_queryset().filter(product_desc__startswith="hdhshjd")
	def product_desc_endswith(self):
		return super(ProductManager,self).get_queryset().filter(product_desc__endswith="2gb")
	def product_desc_fullmatch(self):
		return super(ProductManager,self).get_queryset().filter(product_desc__exact="2gb")
	def product_desc_contains(self):
		return super(ProductManager,self).get_queryset().filter(product_desc__contains="2gb")

	#product method for mrp.
	def product_mrp_one(self):
		return super(ProductManager,self).get_queryset().filter(product_mrp__lte=100)
	def product_mrp_two(self):
		return super(ProductManager,self).get_queryset().filter(product_mrp__gte=100).filter(product_mrp__lt=500)
	def product_mrp_three(self):
		return super(ProductManager,self).get_queryset().filter(product_mrp__gte=500).filter(product_mrp__lt=1000)
	def product_mrp_four(self):
		return super(ProductManager,self).get_queryset().filter(product_mrp__gte=1000).filter(product_mrp__lt=5000)
	def product_mrp_five(self):
		return super(ProductManager,self).get_queryset().filter(product_mrp__gte=5000).filter(product_mrp__lt=10000)
	def product_mrp_six(self):
		return super(ProductManager,self).get_queryset().filter(product_mrp__gt=10000)
	



# Create your Product  models here.
class Products(models.Model):
	product_name		=	models.CharField(max_length = 100)
	product_mrp			=	models.DecimalField(max_digits = 10,decimal_places = 2)
	product_desc		=	models.CharField(max_length = 200)
	product_mfg_date	=	models.DateField()
	product_exp_date	=	models.DateField()
	product_type		=	models.ForeignKey(ProductType,on_delete = models.CASCADE)
	product_image		=	models.ImageField(upload_to = 'product_images', blank = True)
	number_of_products	=	models.IntegerField()
	manager				=	ProductManager()
	#Create model method for expired products here.
	def expired(self):
		if self.product_exp_date==datetime.date.today():
			return "This product expriry date is going to be expired Today."
		elif self.product_exp_date<datetime.date.today():
			return "This product is expired."
		else:
			return "Two years of mfg date"

	#Create model method for any discount products here.
	def price(self):
		if 1000< self.product_mrp <5000:
			price	=	self.product_mrp/100*90
			return price
		elif self.product_mrp>=5000:
			price	=	self.product_mrp/100*80
			return price
		elif self.product_mrp<1000:
			price	=	self.product_mrp/100*95
			return price
	class Meta:
		db_table="Products"
		ordering=("id",)
	def __str__(self):
		return self.product_name+"  "+self.product_desc
class ProductForm(forms.ModelForm):
	class Meta:
		model=Products
		fields="__all__"
#Create product form class here.
class ProductForm(forms.ModelForm):
	class Meta:
		model=Products
		fields='__all__'


# Create your Employee  models here.
class Employee(models.Model):
	first_name			=	models.CharField(max_length = 15)
	middle_name			=	models.CharField(max_length = 15,blank=True)
	last_name			=	models.CharField(max_length = 10)
	father_name			=	models.CharField(max_length = 50)
	gender				=	models.CharField(max_length = 2,choices = gender,default='M')
	dob					=	models.DateField()
	salary				=	models.DecimalField(max_digits = 10,decimal_places = 2)
	join_date			=	models.DateField()
	experience			=	models.IntegerField()
	mail_id				=	models.EmailField(max_length = 100)
	mobile_number		=	models.CharField(max_length = 15)
	address				=	models.CharField(max_length=200)
	image				=	models.ImageField(upload_to = 'Employee_images', blank = True)

	
	#Create model method for employee Birth day wishesh here.
	def greeting(self):
		m=datetime.date.today().month
		d=datetime.date.today().day
		if (self.dob.month==m)and(self.dob.day==d):
			return "Wish you many more happy return of the day."

	#Create model method for age calculation here.
	def age(self):
		today = datetime.date.today()
		years = today.year - self.dob.year
		if today.month < self.dob.month or (today.month == self.dob.month and today.day < self.dob.day):
			years = years-1
			return years
		else:
			return years
	def name(self):
		return self.first_name+" "+self.middle_name+" "+self.last_name

	def __str__(self):
		return self.first_name+" "+self.middle_name+" "+self.last_name
	
	class Meta:
		db_table = "Employee"

#Create your Customer Model here.
class Customer(models.Model):
	first_name			=	models.CharField(max_length = 15)
	middle_name			=	models.CharField(max_length = 15,blank=True)
	last_name			=	models.CharField(max_length = 10)
	gender				=	models.CharField(max_length = 2,choices = gender,default = 'M')
	mail_id				=	models.EmailField(max_length = 100,unique = True)
	mobile_number		=	models.CharField(max_length = 10,unique = True)
	address				=	models.CharField(max_length = 200)
	password			=	models.CharField(max_length	= 12,null=True)
	

	def __str__(self):
		return self.first_name+" "+self.middle_name+" "+self.last_name
	
	class Meta:
		db_table = "Customer"
class CustomerForm(forms.ModelForm):
	class Meta:
		model=Customer
		fields='__all__'