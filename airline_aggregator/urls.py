"""airline_aggregator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from django.urls import path
from aggregator import views

urlpatterns = [
    path('flight_selection/', views.flight_selection, name='flight_selection'),
    path('flight_api/', views.flight_api, name='flight_api'),
    path('create_booking/', views.create_booking, name='create_booking'),
    path('create_bookingapi/', views.create_bookingapi, name='create_bookingapi'),
    path('create_refundapi/', views.create_refundapi, name='create_refundapi'),
    path('create_refund/', views.create_refund, name='create_refund'),
    path('payment_template/', views.payment_template, name='payment_template'),
    path('make_payment/', views.make_payment, name='make_payment'),
    path('cancel_booking/', views.cancel_booking, name='cancel_booking'),
    path('cancel_template/', views.cancel_template, name='cancel_template'),
    path('', views.home, name='home'),
]