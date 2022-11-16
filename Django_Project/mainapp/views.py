from django.shortcuts import render


def mane(request):
    return render(request, 'index.html')
