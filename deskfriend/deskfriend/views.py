from django.shortcuts import render


def home(request):
    return render(request, 'deskfriend/home.html')


def about(request):
    return render(request, 'deskfriend/about.html', {'title': 'About'})
