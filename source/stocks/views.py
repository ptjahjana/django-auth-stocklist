from django.shortcuts import render
from .filters import StockFilter
from .models import Stock

def list(request):
    stocks = Stock.objects.all()
    f = StockFilter(request.GET, queryset=stocks)
    return render(request, 'stocks/index.html', {'filter': f})