from .models import Qrcodes
from django.forms import ModelForm, TextInput


class QrcodesForm(ModelForm):
    class Meta:
        model = Qrcodes
        fields = ["qr_name", "qr_link"]
        widgets = {
            "qr_name": TextInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Например: Мой QR-код:'
        }),
            "qr_link": TextInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Например: https://mail.ru/:'
            }),

        }