from django.db import models

import uuid

class InterestArea(models.Model):
    title       = models.CharField(max_length=120)
    create_date = models.DateTimeField(auto_now_add=True)
    slug        = models.SlugField(max_length=6,unique=True,default="123456")

    class Meta:
        verbose_name = 'Área de Interesse'
        verbose_name_plural = 'Áreas de Interesse'
        ordering = ['create_date','title']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # if not self.id:
        #     self.slug = uuid.uuid4()
        super(InterestArea, self).save(*args, **kwargs)