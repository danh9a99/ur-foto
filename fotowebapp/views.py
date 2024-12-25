from django.http import HttpResponse
from django.template import loader

def index(request): 
    template_name = "fotowebapp/index.html"
    template = loader.get_template(template_name)
    # content = loader.render_to_string(template_name, context)
    return HttpResponse(template.render())