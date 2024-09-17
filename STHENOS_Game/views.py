from django.shortcuts import render

# Create your views here.
def game(request):
    context = {'current_page': 'game'}
    return render (request,"game.html", context)
