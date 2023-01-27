from django.contrib import messages
from django.shortcuts import render,redirect

from pymongo import auth


def Payf(request):
    return render(request,'pay.html')
def Pays(request):
    if request.method == 'POST':
        # Get the form data
       card_number = request.POST.get('cardNumber')
       expiration_date = request.POST.get('expirationDate')
       security_code = request.POST.get('securityCode')
       name_on_card = request.POST.get('nameOnCard')

       messages.info(request,"Successfully paid your amount")
        # check the payment status and do some action
       if not card_number or not expiration_date or not security_code or not name_on_card:
            return render(request,'pay.html', {'error': 'Please fill in all fields.'})

            # Perform any other business logic or database operations here
            # ...

            # Redirect to a success page
       return render(request,'success.html')
    else:
          return render(request,'pay.html')