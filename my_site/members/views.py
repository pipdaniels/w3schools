from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member
# Create your views here.
def members(request):
    template=loader.get_template('all_members.html')
    mymembers = Member.objects.all().values()
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))

def details(request, slug):
    template = loader.get_template('details.html')
    mymember = Member.objects.all().get(slug=slug)
    context = {
        'mymember':mymember,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template=loader.get_template('main.html')
    return HttpResponse(template.render())

def testing(request):
    template = loader.get_template('template.html')
    context = {
        'fruits':['Apple', 'Banana', 'Cherry'],
    }
    return HttpResponse(template.render(context, request))

