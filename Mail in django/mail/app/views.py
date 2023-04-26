from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail


def submit(request):    
    return render(request,'form.html')


def mail(request):
    subject = "WELCOME"
    msg = "Congratulations 😀🆒🐉🦕🦦🐊🐀 for your success"
    to = 'souravyadav040@gmail.com'
    res = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])
    if res == 1:
        msg = 'Email sent successfully!'
    else:
        msg = 'Email could not be sent.'
    return HttpResponse (msg)
