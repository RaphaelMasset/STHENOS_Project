from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def calculators(request):
    user = request.user
    if user.is_authenticated:
        context = {'current_page': 'calculators',
                    'height': request.user.height,
                    'weight': request.user.weight,
                    'wristC': request.user.wristC,
                    'ankleC': request.user.ankleC,
                    'bodyFat': request.user.bodyFat,
                }
    else:
        context = {'current_page': 'calculators',}

    return render (request,"calculators.html", context)