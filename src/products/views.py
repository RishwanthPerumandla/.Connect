from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from .forms import ProductForm, buyerForm
from math import ceil
from django.conf import settings
from django.template.loader import get_template, render_to_string
from django.core.mail import send_mail, BadHeaderError

# Create your views here.
def home_view(request):
	products = Product.objects.all()
	print(products)
	n = len(products)
	
	template='home.html'
	return render(request, template)


def product_create_view(request):
	form = ProductForm(request.POST or None, request.FILES or None)
	if form.is_valid():
	   form.save()
	   form = ProductForm()
	context = {'form': form}
	return render(request, "create.html", context)




def product_detail_view(request):
  products = Product.objects.all()
  params = {'products':products}  
  return render(request, "detail.html", params)


def product_detailed_view(request, my_id):
	if request.method == 'GET':
		form = buyerForm()
	else:
		object1 = Product.objects.get(id=my_id)
		form = buyerForm(request.POST)
		if form.is_valid():
			to_email = str(object1.email)
			img = object1.image
			Phone_Number = form.cleaned_data['Phone_Number']
			subject	='Mail from .Connect'
			name = form.cleaned_data['name']
			title = object1.title
			message = '.'
			from_email	= settings.EMAIL_HOST_USER
			maildyn={
			            'my_id': my_id,
						'name': name,
						'img': img,
						'Phone_Number': Phone_Number,
						'title': title,

					}
			html_message= render_to_string('email.html',maildyn)
		try:
			send_mail(subject,message, from_email, [to_email],html_message=html_message)
		except BadHeaderError:
			return HttpResponse('Invalid header found.')
		return render(request, "buyerForm1.html", {'form': form})

	return render(request, "buyerForm.html", {'form': form})


def product_delete_view(request, my_id):
	if request.method=='GET':
		object2 = Product.objects.get(id=my_id)
		object2.delete()
	return render(request, "deleteview.html" )






