from django.shortcuts import render

def index(request):
    posts = ['First Post', 'Second Post', 'Third Post']
    return render(request, 'index.html', {'posts': posts})