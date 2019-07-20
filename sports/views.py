from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    """ A view to display the index page """
    return render(request, 'index.html')
    
def about(request):
    """ A view to display the index page """
    return render(request, 'about.html')