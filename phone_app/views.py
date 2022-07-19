from django.shortcuts import render, redirect
from phone_app.models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    sorting = {
        'name': 'name',
        'min_price': 'price',
        'max_price': '-price',
        'old_release': 'release_date',
        'new_release': '-release_date',


    }
    get_sort_method = request.GET.get('sort', 'name')
    phones = Phone.objects.order_by(sorting.get(get_sort_method))
    template = 'catalog.html'
    context = {'phones': phones}

    return render(request, template, context)


def show_phone(request, slug):
    phone = Phone.objects.get(slug=slug)
    template = 'sample.html'
    context = {'phone': phone}

    return render(request, template, context)

 