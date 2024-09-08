from django.shortcuts import render
from django.db.models import Sum


from myapp5.models import Product


def total_in_db(request):
    total = Product.objects.aggregate(Sum('quantity'))
    context = {
        'title': 'Total quantity calc in base',
        'total': total,
    }
    return render(request, 'myapp6/total_template.html', context)

def total_in_view(request):
    products = Product.objects.all()
    total = sum(product.quantity for product in products)
    context = {
        'title': 'Total count calc in view',
        'total': total,
    }
    return render(request, 'myapp6/total_template.html', context)

def total_in_template(request):
    context = {
        'title': 'Total count calc in template',
        'products': Product,
    }
    return render(request, 'myapp6/total_template.html', context)

# Create your views here.
