from django.urls import path
from . import views
app_name='payment_app'
urlpatterns=[
    path('Payf',views.Payf,name='Payf'),
    path('Pays/',views.Pays,name='Pays'),
]