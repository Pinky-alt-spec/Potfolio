from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('', views.contact, name='index'),
    path('about', views.about, name='about'),
    path('projects', views.projects, name='projects'),
    path('education-experience', views.edu_Exp, name='education-experience'),
    path('contact', views.contact, name='contact'),

    path('todo', views.todo, name='todo'),
    path('dentist', views.dentist, name='dentist'),
    path('poll', views.poll, name='poll'),
    path('weather', views.weather, name='weather'),
    path('ecommerce', views.ecommerce, name='ecommerce'),
    # path('web-design', views.MyProjects, name='web-design'),

    path('BscCS', views.bscCS, name='Bcs'),
    path('data-developer', views.dataDev, name='data-developer'),
    path('IT-Diploma', views.diploma, name='IT-Diploma'),
    path('it-intern', views.intern, name='it-intern'),
    path('software-developer', views.softwareDev, name='software-developer'),
]