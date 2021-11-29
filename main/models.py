from django.db import models
import qrcode

# filename = "site.png"


class Qrcodes(models.Model):
    qr_name = models.TextField("Название")
    qr_link = models.TextField("Ссылка")
    qr_img = models.ImageField("Изображение", upload_to='media')

    # def __str__(self):
    #     return self.qr_name, self.qr_link, self.qr_img

    def __str__(self):
        template = '{0.qr_name} {0.qr_link} {0.qr_img}'
        return template.format(self)




# пример данных
#
# name = Qrcodes.qr_name
# data = Qrcodes.qr_link
# # имя конечного файла
# # генерируем qr-код
# img = qrcode.make(data)
# # сохраняем img в файл
# img.save(filename)