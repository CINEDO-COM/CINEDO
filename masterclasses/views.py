from django.shortcuts import get_object_or_404, render
from . models import Masterclass


def home(request):
    masterclasses = Masterclass.objects.all()
    context = {
        'masterclasses': masterclasses
    }
    return render (request, 'masterclasses/masterclasses.html', context)

def masterclass(request, masterclass_id):
    masterclass = get_object_or_404(Masterclass, pk=masterclass_id)
    context ={
        'masterclass': masterclass
    }
    return render(request, 'masterclasses/masterclass.html', context)

def tips(request):
    return render (request, 'masterclasses/tips.html')
