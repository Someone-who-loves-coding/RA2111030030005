from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Product

def top_products(request, category_name):
    n = int(request.GET.get('n', 10))
    page = int(request.GET.get('page', 1))
    sort_by = request.GET.get('sort_by', 'rating')
    sort_order = request.GET.get('sort_order', 'desc')

    start_index = (page - 1) * n
    end_index = start_index + n

    if sort_order == 'asc':
        products = Product.objects.filter(category=category_name).order_by(sort_by)[start_index:end_index]
    else:
        products = Product.objects.filter(category=category_name).order_by(f'-{sort_by}')[start_index:end_index]

    data = []
    for product in products:
        data.append({
            'id': product.id,
            'name': product.name,
            'category': product.category,
            'price': product.price,
            'company': product.company,
            'rating': product.rating,
            'discount': product.discount
        })

    return JsonResponse(data, safe=False)

def product_details(request, category_name, product_id):
    product = get_object_or_404(Product, pk=product_id)
    data = {
        'id': product.id,
        'name': product.name,
        'category': product.category,
        'price': product.price,
        'company': product.company,
        'rating': product.rating,
        'discount': product.discount
    }
    return JsonResponse(data)