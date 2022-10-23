from django.shortcuts import render


def contact(request):
    return render(request, 'app/pages/contact.html', {})

def home(request):
    return render(request, 'app/pages/index.html', {})

