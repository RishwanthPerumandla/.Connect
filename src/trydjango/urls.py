"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path


from products import views as products_views
from products.views import product_detail_view, product_create_view, product_detailed_view, product_delete_view


urlpatterns = [
    path('',products_views.home_view,name='home'),
	path('admin/', admin.site.urls),
	path('home/',products_views.home_view,name='home'),
    path('create/', products_views.product_create_view,name='create'),
	path('detail/<int:my_id>/',products_views.product_detailed_view,name='product_detailed_view'),
    path('detail/', products_views.product_detail_view,name='detail'),
    path('email/',products_views.product_detailed_view, name='email'),
    path('delete/<int:id>/',products_views.product_delete_view,name='product_delete_view'),
   
]


if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

