from django.shortcuts import render
from .models import Order
from .froms import OrderForm


# Create your views here.
def f_page(request):
    all_object = Order.objects.all()
    form = OrderForm()
    return render(request, './index.html', {"all_object": all_object,
                                            "form": form})


def ty_page(request):
    name = request.POST['name']
    phone = request.POST['phone']
    element = Order(order_name=name, order_phone=phone)
    element.save()
    return render(request, './thanks.html', {'name ': name,
                                             'phone': phone})
