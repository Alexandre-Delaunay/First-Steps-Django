from django.shortcuts import render
from .Article import Article

def index(request):    
    articles = Article.all()
    return render(request, 'index.html', {'articles': articles})

def show(request, id):
    article = Article.findById(id)
    return render(request, 'show.html', {'article': article})