from django.db import models
from .utils import get_filtered_image
from PIL import Image
import numpy as np
from io import BytesIO
from django.core.files.base import ContentFile
# Create your models here.
ACTION_CHOICES=(
    ('GRAYSCALE','grayscale'),
    ('RED','red'),
    ('GREEN','green'),
    ('BLUE','blue')
)

class Upload(models.Model):
    image = models.ImageField(upload_to="imageCV")
    action = models.CharField(max_length=50,
    choices=ACTION_CHOICES,
    default='GRAYSCALE')
    
    def __str__(self):
	    return self.action

    #PUT BUTTON SAVE
    def save(self,*args,**kwargs):
        
        #open image
        pil_img = Image.open(self.image)
        #conver to image on matriz and realizar  process
        cv_img = np.array(pil_img) # conver to array
        img = get_filtered_image(cv_img,self.action)
        #conver back to pil image
        im_pil = Image.fromarray(img)
        #save
        buffer = BytesIO()
        im_pil.save(buffer,format='png')
        image_png = buffer.getvalue()


        self.image.save(str(self.image),ContentFile(image_png),save=False)

        super().save(*args,**kwargs)