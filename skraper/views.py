from django.shortcuts import render
from django.http import HttpResponse
from . import price
from multiprocessing import Pool
from . skus import skus as sku


def index(request):
    
    return render(request, 'skraper/home.html')

def resolt(request):
    sku = request.GET.get('skus')
    pool = Pool(processes=10)
    sku = sku[1:] if sku[0] == 0 else sku
    prises = pool.map(price.get_price, sku.split(';'))
    
    items = []
    for sku_, price_ in prises:
        items.append({'sku': sku_, 'price': price_})
    return render(request, 'skraper/resolt.html',{'items':items})