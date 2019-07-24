from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from products.models import Product
from .forms import buyerForm


# Create your views here.
def buyerform(request):
		if request.method == 'GET':
			form = buyerForm()
		else:
			object1 = Product.objects.get(id)
			form = buyerForm(request.POST)
			if form.is_valid():
				to_email = str(object1.email)
				img = object1.image
				subject	='Mail from .Connect'
				from_email	= settings.EMAIL_HOST_USER
				context:{
					'name': name,
					'img': img,
					'phone_number':phone_number,

				}
				message	= get_template('email.html').render(context)
			try:
				send_mail(subject, message, from_email, [to_email])
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			
		return render(request, "buyerForm.html", {'form': form})


