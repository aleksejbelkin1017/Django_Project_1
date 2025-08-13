from django.core.exceptions import ValidationError
from django.forms import ModelForm, BooleanField
from django.utils.translation import gettext_lazy as _

from catalog.models import Product

FORBIDDEN_WORDS = [
    'казино',
    'криптовалюта',
    'крипта',
    'биржа',
    'дешево',
    'бесплатно',
    'обман',
    'полиция',
    'радар'
]


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs['class'] = "form-check-input"
            else:
                fild.widget.attrs['class'] = "form-control"


class ProductForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        exclude = ('created_at', 'updated_at')

    def clean_price(self):
        price = self.cleaned_data['price']
        if price < 0:
            raise ValidationError("Цена не может быть меньше 0!")
        return price

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('name', '').lower()
        description = cleaned_data.get('description', '').lower()

        # Проверяем наличие запрещённых слов в названии
        for word in FORBIDDEN_WORDS:
            if word in title:
                self.add_error('name', ValidationError(
                    _('Запрещённое слово в названии: %(word)s'),
                    params={'word': word}
                ))

        # Проверяем наличие запрещённых слов в описании
        for word in FORBIDDEN_WORDS:
            if word in description:
                self.add_error('description', ValidationError(
                    _('Запрещённое слово в описании: %(word)s'),
                    params={'word': word}
                ))

        return cleaned_data