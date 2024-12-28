from django.http import HttpResponse
from django.template import loader

def index(request):
    template_name = "fotowebapp/index.html"
    template = loader.get_template(template_name)
    return HttpResponse(template.render())

def galary(request): 
    template_name = "fotowebapp/galary.html"
    template = loader.get_template(template_name)
    return HttpResponse(template.render())

def login(request):
    template_name = "fotowebapp/login.html"
    template = loader.get_template(template_name)
    return HttpResponse(template.render())

def register(request):
    template_name = "fotowebapp/register.html"
    template = loader.get_template(template_name)
    return HttpResponse(template.render())

def blog(request):
    template_name = "fotowebapp/blog.html"
    template = loader.get_template(template_name)
    return HttpResponse(template.render())