from django.db import models
from .utils import get_filtered_image
from PIL import Image
import numpy as np
from io import BytesIO
from django.core.files.base import ContentFile
import datetime
# Create your models here.
ACTION_CHOICES=(
    ('OPERADOR_IDENTIDAD','operador_identidad'),
    ('OPERADOR_INVERSO','operador_inverso'),
    ('OPERADOR_UMBRAL','operador_umbral'),
    ('OPERADOR_UMBRAL_INVERSO','operador_umbral_inverso'),
    ('OPERADOR_UMBRAL_BINARIO','operador_umbral_binario'),
    ('OPERADOR_UMBRAL_BINARIO_INVERSO','operador_umbral_binario_inverso'),
    ('OPERADOR_ESCALA_GRISES','operador_escala_grises'),
    ('OPERADOR_ESCALA_GRISES_INVERTIDO','operador_escala_grises_invertido'),
    ('OPERADOR_EXTENSION','operador_extension'),
    ('OPERADOR_REDUCCION_GRISES','operador_reduccion_grises')
)

class Upload(models.Model):
    image = models.ImageField(upload_to="image")
    start_date = models.DateTimeField(default=datetime.datetime.now())
    action = models.CharField(max_length=255,
    choices=ACTION_CHOICES,
    default='OPERADOR_IDENTIDAD')
    
    
    def __str__(self):
        return self.action

    #PUT BUTTON SAVE
    def save(self,*args,**kwargs):
        #open image
        pil_img = Image.open(self.image).convert("L")
        img = get_filtered_image(pil_img,self.action)
        #save
        buffer = BytesIO()
        img.save(buffer,format='png')
        image_png = buffer.getvalue()
        self.image.save(str(self.image),ContentFile(image_png),save=False)

        super().save(*args,**kwargs)