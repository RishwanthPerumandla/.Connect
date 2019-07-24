from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from .forms import ProductForm
from math import ceil	
from django.conf import settings
from buyerform.forms import buyerForm
from django.template.loader import get_template, render_to_string
from django.core.mail import send_mail, BadHeaderError

# Create your views here.
def home_view(request):
	products = Product.objects.all()
	print(products)
	n = len(products)
	nSlides = n//4 + ceil((n/4)-(n//4))
	params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'product': products}
	template='home.html'
	return render(request, template, params)


def product_create_view(request):
	form = ProductForm(request.POST or None, request.FILES or None)
	if form.is_valid():
	   form.save()
	   form = ProductForm()
	context = {'form': form}
	return render(request, "create.html", context)



def product_detail_view(request):
	allProds = []
	catprods = Product.objects.values('category', 'id')
	cats = {item['category'] for item in catprods}
	for cat in cats:
		prod = Product.objects.filter(category=cat)
		n = len(prod)
		nSlides = n // 4 + ceil((n / 4) - (n // 4))
		allProds.append([prod, range(1, nSlides), nSlides])
		params = {'allProds':allProds}
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
			message = '.'
			from_email	= settings.EMAIL_HOST_USER
			maildyn={
						'name': name,
						'img': img,
						'Phone_Number': Phone_Number,
						
					}
			html_message= render_to_string('email.html',maildyn)
		try:
			send_mail(subject,message, from_email, [to_email],html_message=html_message)
		except BadHeaderError:
			return HttpResponse('Invalid header found.')
		return HttpResponse('Thanks your details are noted')
		
	return render(request, "buyerForm.html", {'form': form})
  
    
def product_delete_view(request, my_id):
	if request.method=='GET':
		object2 = Product.objects.get(id=my_id)
		object2.delete()
	return HttpResponse('your product has been deleted')




