from django.shortcuts import render
from .models import Qrcodes
from .forms import QrcodesForm
import qrcode
from django.conf import settings

import random
import string


# def generate_random_string(length):
#     letters = string.ascii_lowercase
#     rand_string = ''.join(random.choice(letters) for i in range(length))
#     return rand_string


def index(request):
    qrcodes = Qrcodes.objects.all()
    return render(request, 'main/index.html', {'qrcodes': qrcodes})


def create(request):
    qr_name = ""
    qr_link = ""
    qr_img = ""
    if request.method == 'POST':
        form = QrcodesForm(request.POST)
        if form.is_valid():
            qr_name = form.cleaned_data.get("qr_name")
            qr_link = form.cleaned_data.get("qr_link")
            name = qr_name
            data = qr_link
            filename = name + ".png"
            img = qrcode.make(data)
            path = 'media/media/' + filename
            img.save(path)
            form = Qrcodes(qr_name=qr_name, qr_link=qr_link, qr_img='media/'+filename)
            # qr_img = form.cleaned_data.get("path")
            form.save()
    form = QrcodesForm()
    context = {
        'form': form,
        'qr_name': qr_name,
        'qr_link': qr_link,
        'qr_img': qr_img
    }
    return render(request, 'main/create.html', context)
