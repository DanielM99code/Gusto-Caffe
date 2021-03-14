from django.shortcuts import render, redirect
from .models import *
from .forms import FormMessage

# Create your views here.
def main_page_view(request):

    if request.method == 'POST':
        form = FormMessage(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    categories = Category.objects.filter(is_visible=True).order_by('category_order')
    for item in categories:
        dishes = Dish.objects.filter(category=item.pk).filter(is_visible=True).order_by('dish_order')
        item.dishes = dishes

    special = Dish.objects.filter(category__title='Special')

    story = Story.objects.all()

    chef = Chef.objects.filter(title='Our chef')

    phone = Phone.objects.all()

    address = Address.objects.all()

    opening_hours = OpeningHours.objects.all()

    cafeinfo = CafeInfo.objects.all()

    message = Message.objects.all()

    form = FormMessage

    return render(request, 'index.html', context={
            'categories': categories,
            'special': special,
            'story': story[0],
            'chef': chef,
            'phone': phone,
            'address': address,
            'opening_hours': opening_hours,
            'cafeinfo': cafeinfo,
            'message': message[0],
            'form': form
        })

def dish_page_view(request, pk):
    dish = Dish.objects.get(pk=pk)
    return render(request, 'dish_info.html', context={'dish': dish})

