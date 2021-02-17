from django.shortcuts import render
#importing email functionality
from django.core.mail import send_mail

# Create your views here.
def contact(request):
    #if the request is a post request
    if request.method == "POST": 
        #html inputs assigned to variables matching the names
        message_name = request.POST['message-name']
        message_email  = request.POST['message-email'] 
        message_subject = request.POST['message-subject']
        message_text = request.POST['message-text']

        #send email 
        send_mail(  
            message_subject, #subject
            message_text, #message
            message_email, #from email
            ['andre.vasquez.14@gmail.com'], #to email 
            )

        return render(request,'contact_form/contact.html',{'message_name': message_name})

    else:
        return render(request,'contact_form/contact.html',{})