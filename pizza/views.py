from .models import Pizza
from django.http import JsonResponse

def get_pizzas(request):
    pizzas = Pizza.objects.all()
    pizza_names = []

    for pizza in pizzas:
        pizza_names.append({
            "id": pizza.id,
            "name": pizza.name,
            "priceHUF": pizza.price,
            "priceEUR": round(pizza.price / 380)
        })
    return JsonResponse({"pizzas":pizza_names})

def get_pizza_by_id(request, id):
    try:
        pizza = Pizza.objects.get(id=id)
        return JsonResponse({
                "id": pizza.id,
                "name": pizza.name,
                "priceHUF": pizza.price,
                "priceEUR": round(pizza.price / 380)
        })
    except:
        return JsonResponse({"message":"Nincs ilyen pizza!"})