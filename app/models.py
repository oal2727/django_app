from django.db import models
from .utils import get_filtered_image
from .utilsOperador import filterImageEdge
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

ACTION_CHOICES_OPERADOR=(
    ('OPERADOR_ROBERTS','operador_roberts'),
    ('OPERADOR_PREWITT','operador_prewitt'),
    ('OPERADOR_SOBEL','operador_sobel'),
    ('OPERADOR_CANNY','operador_canny'),
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
        #convert the image to array
        cv_img = np.array(pil_img)
        img = get_filtered_image(cv_img,self.action)
        #save
        buffer = BytesIO()
        img.save(buffer,format='png')
        image_png = buffer.getvalue()
        self.image.save(str(self.image),ContentFile(image_png),save=False)

        super().save(*args,**kwargs)



class OperatorEdge(models.Model):
    imageoperator = models.ImageField(upload_to="edge")
    start_date = models.DateTimeField(default=datetime.datetime.now())
    action = models.CharField(max_length=255,
    choices=ACTION_CHOICES_OPERADOR,
    default='OPERADOR_ROBERTS')

    def __str__(self):
        return self.action
    
    def save(self,*args,**kwargs):
        #open image
        pil_img = Image.open(self.imageoperator)
        
        cv_img = np.array(pil_img)
        img = filterImageEdge(cv_img,self.action)
        
        #convert back to pil image
        im_pill = Image.fromarray(img)

        #save
        buffer = BytesIO()
        im_pill.save(buffer,format='png')
        image_png = buffer.getvalue()

        self.imageoperator.save(str(self.imageoperator),ContentFile(image_png),save=False)
        # -------
        super().save(*args,**kwargs)