from django.shortcuts import render
from .models import *
from .forms import *

from django.shortcuts import redirect

from django.shortcuts import render, get_object_or_404

from django.contrib.auth.decorators import login_required
now = timezone.now()
def home(request):
    return render(request, 'portfolio/home.html',
                  {'portfolio': home})

@login_required
def customer_list(request):
    customer = Customer.objects.filter(created_date__lte=timezone.now())
    return render(request, 'portfolio/customer_list.html',
                 {'customers': customer})

# Create your views here.

@login_required
def customer_edit(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == "POST":
        # update
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.updated_date = timezone.now()
            customer.save()
            customer = Customer.objects.filter(created_date__lte=timezone.now())
            return render(request, 'portfolio/customer_list.html',
                          {'customers': customer})
    else:
        # edit
        form = CustomerForm(instance=customer)
    return render(request, 'portfolio/customer_edit.html', {'form': form})


@login_required
def customer_delete(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    customer.delete()
    return redirect('portfolio:customer_list')


@login_required
def stock_list(request):
    stocks = Stock.objects.filter(purchase_date__lte=timezone.now())
    return render(request, 'portfolio/stock_list.html', {'stocks': stocks})


@login_required
def stock_new(request):
    if request.method == "POST":
        form = StockForm(request.POST)
        if form.is_valid():
            stock = form.save(commit=False)
            stock.created_date = timezone.now()
            stock.save()
            stocks = Stock.objects.filter(purchase_date__lte=timezone.now())
            return render(request, 'portfolio/stock_list.html',
                          {'stocks': stocks})
    else:
        form = StockForm()
        # print("Else")
    return render(request, 'portfolio/stock_new.html', {'form': form})


@login_required
def stock_edit(request, pk):
    stock = get_object_or_404(Stock, pk=pk)
    if request.method == "POST":
        form = StockForm(request.POST, instance=stock)
        if form.is_valid():
            stock = form.save()
            # stock.customer = stock.id
            stock.updated_date = timezone.now()
            stock.save()
            stocks = Stock.objects.filter(purchase_date__lte=timezone.now())
            return render(request, 'portfolio/stock_list.html', {'stocks': stocks})
    else:

        form = StockForm(instance=stock)
    return render(request, 'portfolio/stock_edit.html', {'form': form})



@login_required
def stock_delete(request, pk):
    customer = get_object_or_404(Stock, pk=pk)
    customer.delete()
    return redirect('portfolio:stock_list')



@login_required
def investor_list(request):
    customer = Investment.objects.filter()
    return render(request, 'portfolio/investment_list.html',
                  {'customers': customer})

# Create your views here.

@login_required
def investor_edit(request, pk):
    customer = get_object_or_404(Investment, pk=pk)
    if request.method == "POST":
        # update
        form = InvestmentForm(request.POST, instance=customer)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.updated_date = timezone.now()
            customer.save()
            customer = Investment.objects.filter()
            return render(request, 'portfolio/investment_list.html',
                          {'customers': customer})
    else:
        # edit
        form = InvestmentForm(instance=customer)
    return render(request, 'portfolio/investment_edit.html', {'form': form})


@login_required
def investor_delete(request, pk):
    customer = get_object_or_404(Investment, pk=pk)
    customer.delete()
    return redirect('portfolio:investment_list')



@login_required
def investor_new(request):
    if request.method == "POST":
        form = InvestmentForm(request.POST)
        if form.is_valid():
            stock = form.save(commit=False)
            stock.created_date = timezone.now()
            stock.save()
            stocks = Stock.objects.filter(purchase_date__lte=timezone.now())
            return render(request, 'portfolio/investment_list.html',
                          {'stocks': stocks})
    else:
        form = InvestmentForm()
        # print("Else")
    return render(request, 'portfolio/investment_new.html', {'form': form})
