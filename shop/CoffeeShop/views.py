from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import OrderForm
from .models import Order

# Create your views here.
def order_view(request):
    submitted = False
    if request.method == "POST":
        form = OrderForm(request.POST)
        form.save()
        return HttpResponseRedirect('?submitted=True')
    else:
        form = OrderForm()
        if 'submitted' in request.GET:
            submitted = True
    context = {'form':form,'submitted':submitted }
    return render(request,'home.html',context)

def orders_list_view(request):
    order_list = Order.objects.all()
    context = {"order_list":order_list}
    return render(request, 'orders.html', context)