from django.shortcuts import render
from . models import Book, Author, Rate
from django.http import HttpResponse
import json
# Create your views here.
def all(request):
    pass

def index(request):
    users = Author.objects.all().values()  # or simply .values() to get all fields
    users_list = list(users)  # important: convert the QuerySet to a list object
    return HttpResponse(json.dumps(users_list), content_type='application/json')
    # return JsonResponse(users_list, safe=False)


def all(request):
    users = Author.objects.all().values()  # or simply .values() to get all fields
    users_list = list(users)  # important: convert the QuerySet to a list object
    return HttpResponse(json.dumps(users_list), content_type='application/json')
    # return JsonResponse(users_list, safe=False)

def show(request, pk):
    users = Author.objects.filter(pk=1).values()  # or simply .values() to get all fields
    users_list = list(users)  # important: convert the QuerySet to a list object
    return HttpResponse(json.dumps(users_list), content_type='application/json')
    # return JsonResponse(users_list, safe=False)


