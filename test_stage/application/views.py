from django.shortcuts import render

# Create your views here.
# application/views.py
from django.shortcuts import render
from .models import Category
from .models import Product
from django.shortcuts import redirect

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

# Ajoutez d'autres vues pour les fonctionnalités supplémentaires
def category_detail(request, category_id):
    category = Category.objects.get(id=category_id)

    return render(request, 'category_detail.html', {'category': category})

def category_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        #create a new category
        category = Category(name=name)
        category.save()
        return redirect('category_list')
    return render(request, 'category_form.html')


def product_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        category_id = request.POST.get('category')
        category = Category.objects.get(id=category_id)
        product = Product(name=name, description=description, price=price, category=category)
        product.save()
        return redirect('category_list')
    categories = Category.objects.all()
    return render(request, 'product_form.html', {'categories': categories})




def category_detail(request, category_id):
    category = Category.objects.get(id=category_id)
    products = Product.objects.filter(category=category)
    return render(request, 'category_detail.html', {'category': category, 'products': products})




