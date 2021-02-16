from django.shortcuts import render

# Create your views here.
def contact(request):
    return render(request,'contact_form/contact.html')