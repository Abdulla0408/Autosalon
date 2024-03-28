from django.shortcuts import render
from django.http import HttpResponse

from .models import Brand, BrandCategory, Color, ColorCategory, Car, CarCategory

# Create your views here.


def all_posts(request):
    posts = Brand.objects.all()
    categories = BrandCategory.objects.all()
    context = {
        'posts': posts,
        'categories': categories,
        'title': "Barcha maqolalar"
    }
    return render(request, 'blog/index.html', context=context)


def posts_by_category(request, category_id):
    posts = Brand.objects.filter(category_id=category_id)
    categories = BrandCategory.objects.all()
    category = BrandCategory.objects.get(pk=category_id)
    context = {
        'posts': posts,
        'categories': categories,
        'title': f"{category.title} ga tegishli maqolalar"
    }
    return render(request, 'blog/index.html', context=context)


# --------------------------------------------------------------------------------------


def all_posts(request):
    posts = Color.objects.all()
    categories = ColorCategory.objects.all()
    context = {
        'posts': posts,
        'categories': categories,
        'title': "All articles"
    }
    return render(request, 'blog/index.html', context=context)


def posts_by_category(request, category_id):
    posts = Color.objects.filter(category_id=category_id)
    categories = ColorCategory.objects.all()
    category = ColorCategory.objects.get(pk=category_id)
    context = {
        'posts': posts,
        'categories': categories,
        'title': f"{category.title} articles related to"
    }
    return render(request, 'blog/index.html', context=context)


# ------------------------------------------------------------------------------------------------


def all_posts(request):
    posts = Car.objects.all()
    categories = CarCategory.objects.all()
    context = {
        'posts': posts,
        'categories': categories,
        'title': "All articles"
    }
    return render(request, 'blog/index.html', context=context)


def posts_by_category(request, category_id):
    posts = Car.objects.filter(category_id=category_id)
    categories = CarCategory.objects.all()
    category = CarCategory.objects.get(pk=category_id)
    context = {
        'posts': posts,
        'categories': categories,
        'title': f"{category.title} articles related to"
    }
    return render(request, 'blog/index.html', context=context)

