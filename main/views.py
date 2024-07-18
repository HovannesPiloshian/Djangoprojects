from django.shortcuts import render
from .models import Electronic
# Create your views here.


def index(request):
    electronic_list = Electronic.objects.all()
    return render(request, 'index.html', context={
        'list':electronic_list
    })

def index_info(request, id):
    my_item = Electronic.objects.get(pk=id)
    return render(request, 'index_info.html', context={
        'my_item':my_item
    })