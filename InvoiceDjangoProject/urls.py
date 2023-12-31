"""
URL configuration for InvoiceDjangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('invoices/',views.invoice , name='invoice'),
    path('invoices/<int:pk>',views.invoice_details , name='invoice_details'),

    path('create/',views.create , name='create'),
    path('save-create/',views.save_create , name='save_create'),


    path('update/<int:pk>',views.invoice_update , name='invoice_update'),
    path('save/<int:pk>',views.save_update , name='save_update')
    
]
