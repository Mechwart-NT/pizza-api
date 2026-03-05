from .models import Pizza
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

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

def endpoints(request):
    data = {
        "pizza/":"Visszaadja az összes pizzát.",
        "pizza/[id]":"Visszad egy pizzát az id alapján.",
        "admin/":"Belépés az admin felületre."
    }

    return JsonResponse(data)

@csrf_exempt
def test_rest(request):
    if request.method == "GET":
        return JsonResponse({"message":"Le akarsz kérdezni valamit?"})
    elif request.method == "POST":
        return JsonResponse({"message":"Létre akarsz hozni valamit?"})
    elif request.method == "DELETE":
        return JsonResponse({"message":"Ki akarsz törölni valamit?"})
    elif request.method == "PUT":
        return JsonResponse({"message":"Módosítani akarsz valamit?"})
    else:
        return JsonResponse({"message":"Bocsi ezt nem ismerem..."})