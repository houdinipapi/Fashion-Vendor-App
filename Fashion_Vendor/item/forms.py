from django import forms

from .models import Item

INPUT_CLASSES = "w-full py-4 px-6 rounded-xl border border-gray-300 bg-gray-100 focus:bg-white focus:outline-none"

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ("category", "name", "description", "price", "image",)

        widgets = {
            "category": forms.Select(attrs={
                "class": INPUT_CLASSES,
            }),
            "name": forms.TextInput(attrs={
                "class": INPUT_CLASSES,
                "placeholder": "Item name",
            }),
            "description": forms.Textarea(attrs={
                "class": INPUT_CLASSES,
                "placeholder": "Item description",
            }),
            "price": forms.TextInput(attrs={
                "class": INPUT_CLASSES,
                "placeholder": "Item price",
            }),
            "image": forms.FileInput(attrs={
                "class": INPUT_CLASSES,
            }),
        }