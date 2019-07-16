from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return HttpResponse('placeholder to later display a list of all blogs')

def new(request):
    return HttpResponse('placeholder to display a new form to create a new blog')

def create(request):
    print('create route hit, redirecting to ////////// ...')
    return redirect('/')

def show(request, number):
    print('the number route is running///////////')
    return HttpResponse(f'placeholder to display blog number: {number}')

def edit(request, number):
    print('the edit route is running/////////////')
    return HttpResponse(f'placeholder to edit blog {number}')

def destroy(request, number):
    print(f'route to delete blog number {number}')
    print('*'*50)
    return redirect('/')