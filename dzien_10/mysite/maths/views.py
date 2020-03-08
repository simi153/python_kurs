from django.shortcuts import render
from django.http import HttpResponse

from maths.models import Math


def index(request):
    return HttpResponse(f"Witaj!")


def add(request, a=0, b=0):
    Math.objects.create(operation="add", a=a, b=b)
    operacja = f"{a}+{b}"
    result = int(a) + int(b)
    return render(request, 'maths/result.html', {"operacja": operacja, "result": result, "title": "Dodawanie"})


def sub(request, a=0, b=0):
    Math.objects.create(operation="sub", a=a, b=b)
    operacja = f"{a}-{b}"
    result = int(a) - int(b)
    return render(request, 'maths/result.html', {"operacja": operacja, "result": result, "title": "Odejmowanie"})


def mul(request, a=0, b=0):
    Math.objects.create(operation="mul", a=a, b=b)
    operacja = f"{a}*{b}"
    result = int(a) * int(b)
    return render(request, 'maths/result.html', {"operacja": operacja, "result": result, "title": "Mnożenie"})


def div(request, a=0, b=1):
    if int(b) == 0:
        return HttpResponse("Nie dzielimy przez 0!")
    else:
        Math.objects.create(operation="div", a=a, b=b)
        operacja = f"{a}/{b}"
        result = int(a) / int(b)
        return render(request, 'maths/result.html', {"operacja": operacja, "result": result, "title": "Dzielenie"})


def sqrt(request, a=0, b=0):
    if int(b) < 2:
        return "Zacznij od pierwiastka 2-giego stopnia"
    else:
        Math.objects.create(operation="sqrt", a=a, b=b)
        operacja = f"pierwiastek {b} stopnia z {a}"
        result = int(a) ** (1 / int(b))
        return render(request, 'maths/result.html',
                      {"operacja": operacja, "result": result, "title": "Pierwiastkowanie"})


def pow_view(request, a=0, b=0):
    Math.objects.create(operation="pow", a=a, b=b)
    operacja = f"{a}^{b}"
    result = int(a) ** int(b)
    return render(request, 'maths/result.html', {"operacja": operacja, "result": result, "title": "Potegowanie"})


# Create your views here.

def lista_elementow(request):

    elementy = Math.objects.all()
    return render(request, 'maths/lista.html', {"elements": elementy})
