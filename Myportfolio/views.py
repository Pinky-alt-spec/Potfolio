from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.core.mail import send_mail
from django.conf import settings


def index(request):
    pass
    # return render(request, 'Myportfolio/index.html')

def about(request):
    return render(request, 'Myportfolio/about-me.html')


def projects(request):
    return render(request, 'Myportfolio/my-projects.html')


def edu_Exp(request):
    return render(request, 'Myportfolio/education-experience-1.html')


def todo(request):
    return render(request, 'Myportfolio/my-projects/todo.html')


def weather(request):
    return render(request, 'Myportfolio/my-projects/weather.html')


def dentist(request):
    return render(request, 'Myportfolio/my-projects/dentist.html')


def poll(request):
    return render(request, 'Myportfolio/my-projects/poll.html')


def ecommerce(request):
    return render(request, 'Myportfolio/my-projects/ecommerce.html')


def bscCS(request):
    return render(request, 'Myportfolio/education-experience-1/BscCS.html')


def dataDev(request):
    return render(request, 'Myportfolio/education-experience-1/data-developer.html')


def diploma(request):
    return render(request, 'Myportfolio/education-experience-1/IT-Diploma.html')


def intern(request):
    return render(request, 'Myportfolio/education-experience-1/it-intern.html')


def softwareDev(request):
    return render(request, 'Myportfolio/education-experience-1/SoftwareDeveloper.html')


def contact(request):
    # grab the information filled by the user
    if request.method == 'POST':
        contact_message = request.POST['contact_message']
        contact_email = request.POST['contact_email']
        # send an email
        send_mail(
            contact_email,
            contact_message,
            settings.EMAIL_HOST_USER,
            ['pinkymononyane@gmail.com'],  # To email
            fail_silently=False
            )

        return render(request, 'Myportfolio/contact-me.html', {'contact_email': contact_email})
    else:
        return render(request, 'Myportfolio/contact-me.html', {})






