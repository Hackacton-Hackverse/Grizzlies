from django.shortcuts import render

def index(request):
    return render(request, 'HackVerse_2024/index.html')