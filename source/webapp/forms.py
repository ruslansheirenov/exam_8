from django import forms
from django.core.exceptions import ValidationError

from webapp.models import Product, Review


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ("title", "description", "category", "picture",)

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data['title']
        description = cleaned_data['description']
        if len(title) < 5:
            self.add_error('title', ValidationError(
                f"Значение должно быть длиннее 5 символов {title} не подходит"))
        if title == description:
            raise ValidationError("Text of the product should not duplicate it's title!")
        return cleaned_data


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ("content", "product", "rating", "check_moder",)


class ProductDeleteForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ("title",)

    def clean_title(self):
        if self.instance.title != self.cleaned_data.get("title"):
            raise ValidationError("Название товара не соответствует")
        return self.cleaned_data.get("title")