from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import DeleteView, UpdateView, CreateView
from django.shortcuts import render, redirect
from main_gusto.forms import Message
from main_gusto.models import Dish, Category
from django.urls import reverse_lazy
from django.contrib import messages
from main_gusto.forms import Message
from main_gusto.models import Category
from .forms import CategoryForm, DishForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from braces.views import GroupRequiredMixin

def is_member(user):
    return user.groups.filter(name='manager').exists() or \
           user.is_staff

@login_required(login_url='/login/')
@user_passes_test(is_member)
def list_of_messages(request):
    messages = Message.objects.filter(is_processed=False).order_by('pub_date')
    paginator = Paginator(messages, 2)
    page = request.GET.get('page')
    messages = paginator.get_page(page)
    return render(request, 'messages.html', context={'messages':messages})

@login_required(login_url='/login/')
@user_passes_test(is_member)
def update_message(request, pk):
    Message.objects.filter(pk=pk).update(is_processed=True)
    return redirect('/admin-panel/messages/')

@login_required(login_url='/login/')
@user_passes_test(is_member)
def list_of_dishes(request):
    dishes = Dish.objects.all()
    return render(request, 'dishes.html', context={'dish': dishes})


class DishAddView(LoginRequiredMixin, GroupRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = ["manager", 'admin']
    model = Dish
    form_class = DishForm
    template_name = 'dish_add.html'
    success_url = reverse_lazy('list_of_dishes')
    success_message = 'Dish has been successfully created!'


class DishDeleteView(LoginRequiredMixin, GroupRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = ["manager", 'admin']
    model = Dish
    success_url = reverse_lazy('list_of_dishes')

    def get(self, request, *args, **kwargs):
        messages.success(request, 'Dish has been deleted successfully!')
        return self.post(request, *args, **kwargs)


class DishUpdateView(LoginRequiredMixin, GroupRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = ["manager", 'admin']
    model = Dish
    form_class = DishForm
    template_name = 'dish_update.html'
    success_url = reverse_lazy('list_of_dishes')
    success_message = 'Dish has been changed successfully!'

@login_required(login_url='/login/')
@user_passes_test(is_member)
def list_of_categories(request):
    items = Category.objects.all().order_by('category_order')
    return render(request, 'categories.html', context={'items': items})

class CategoryAddView(LoginRequiredMixin, GroupRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = ["manager", 'admin']
    model = Category
    form_class = CategoryForm
    template_name = 'category_add.html'
    success_url = reverse_lazy('list_of_categories')
    success_message = 'Category has been successfully created!'

class CategoryDeleteView(LoginRequiredMixin, GroupRequiredMixin,DeleteView):
    login_url = reverse_lazy('login')
    group_required = ["manager", 'admin']
    model = Category
    success_url = reverse_lazy('list_of_categories')

    def get(self, request, *args, **kwargs):
        messages.success(request, 'Category deleted successfully!')
        return self.post(request, *args, **kwargs)

class CategoryUpdateView(LoginRequiredMixin, GroupRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = ["manager", 'admin']
    model = Category
    form_class = CategoryForm
    template_name = 'category_update.html'
    success_url = reverse_lazy('list_of_categories')
    success_message = 'Category changed successfully!'
