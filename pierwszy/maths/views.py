from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template.loader import get_template

from maths.models import Math




def calculate(request, op, a, b,):
    operations = {
        "add": lambda x, y: x+y,
        "sub": lambda x, y: x-y,
        "mul": lambda x, y: x*y,
        "div": lambda x, y: x/y,
    }
    try:
        resault = operations[op](a, b)
    except ZeroDivisionError:
        resault = "Działanie niemożliwe"

    Math.objects.create(
        operation=op,
        a=a,
        b=b,
        resault=resault
    )
    return HttpResponse(resault)

def history(request):
    maths = Math.objects.all()
    template = get_template("maths/math_history.html")
    context = {"maths": maths, "text": "Ala ma kota"}
    return HttpResponse(template.render(context=context))

    # return render(
    #     request=request,
    #     template_name="maths/math_history.html",
    #     context=context
    # )

def history_detail(request, id):
    m = Math.objects.get(id=id)
    return render(
        request=request,
        template_name = "maths/math_detail.html",
        context = {"maths": m}
    )