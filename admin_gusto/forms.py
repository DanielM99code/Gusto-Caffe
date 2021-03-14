from django import forms
from main_gusto.models import Category, Dish



class CategoryForm(forms.ModelForm):
    title = forms.CharField(max_length=15,
                            widget=forms.TextInput(attrs={'placeholder': "Название", 'required': "required"}))
    category_order = forms.IntegerField(
        widget=forms.TextInput(attrs={'placeholder': "Порядок категории в меню", 'required': "required"}))
    photo = forms.ImageField(widget=forms.FileInput())
    is_visible = forms.BooleanField(initial=True, required=False)

    class Meta:
        model = Category
        fields = ('title', 'photo', 'category_order', 'is_visible')

class DishForm(forms.ModelForm):
    title = forms.CharField(max_length=25,
                            widget=forms.TextInput(attrs={'placeholder': "Name", 'required': "required"}))
    photo = forms.ImageField(widget=forms.FileInput())
    dish_order = forms.IntegerField(
        widget=forms.TextInput(attrs={'placeholder': "Dish order in menu", 'required': "required"}))
    is_visible = forms.BooleanField(initial=True, required=False)
    price = forms.DecimalField(max_digits=6, decimal_places=2,
                               widget=forms.TextInput(attrs={'placeholder': "Dish price", 'required': "required"}))
    desc = forms.CharField(max_length=150,
                           widget=forms.TextInput(attrs={'placeholder': "Description", 'required': "required"}))
    category = forms.ModelChoiceField(queryset=Category.objects.all())

    class Meta:
        model = Dish
        fields = ('title', 'photo', 'dish_order', 'is_visible', 'price', 'desc', 'category')
