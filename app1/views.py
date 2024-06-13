from django.shortcuts import render
from django.template import loader, Template, context
from django.http import HttpResponse

from .models import Member

def testing(request):
    mydata = Member.objects.all()
    template = loader.get_template('model.html')
    context = {
        'members': mydata,
    }
    return HttpResponse(template.render(context, request))

