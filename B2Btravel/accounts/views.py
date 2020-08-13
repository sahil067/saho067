from django.shortcuts import render, redirect
from accounts.models import Contact

# Create your views here.


def accounts(request):
    # return HttpResponse("This is my homepage(/)")
    context = {'name': 'B2B Travel'}
    return render(request, 'accounts.html', context)


def Dashboard(request):
    # return HttpResponse("This is my about page (/about)")
    return render(request, 'Dashboard.html')


def OnlineBooking(request):
    # return HttpResponse("This is my projects page (/projects)")
    return render(request, 'Booking.html')


def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        #print(name, email, phone, desc)
        ins = Contact(name=name, email=email, phone=phone, desc=desc)
        ins.save()
        print("this data has return to db")

    # return HttpResponse("This is my contact page(/contact)")
    return render(request, 'contact.html')
