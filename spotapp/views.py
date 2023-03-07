from django.shortcuts import render, get_object_or_404, redirect
from .models import Drink, Review
from django.http import JsonResponse
from django.contrib import messages
# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def drinks(request):
    context = {
        "jugos": Drink.objects.filter(drink_tag="JUGO"),
        "mojitos": Drink.objects.filter(drink_tag="MOJITIO"),
        "hotdrinks": Drink.objects.filter(drink_tag="HOTDRINKS")
    }
    return render(request, 'drinks.html', context=context)


def drink_detail(request, drink_id):

    drink = get_object_or_404(Drink, id=drink_id)
    if drink.drink_tag == 'HOTDRINKS':
        pill_bg_color = 'bg-orange-200'
    elif drink.drink_tag == 'JUGO':
        pill_bg_color = 'bg-blue-200'
    elif drink.drink_tag == 'MOJITIO':
        pill_bg_color = 'bg-purple-200'
    else:
        pill_bg_color = 'bg-yellow-200'

    if request.method == 'POST':
        rating = int(request.POST['rating'])
        new_rating = Review(drink=drink, rate=rating)
        new_rating.save()
        messages.success(request, "Your Review has been added! 😁")
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
    context = {
        'drink': get_object_or_404(Drink, id=drink_id),
        'bg_color': pill_bg_color,
    }
    return render(request, 'drink_detail.html', context)
