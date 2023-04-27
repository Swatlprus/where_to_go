from django.shortcuts import render


def show_maps(request):
    return render(request, 'index.html')
