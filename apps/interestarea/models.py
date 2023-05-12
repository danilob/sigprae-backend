from django.db import models

import uuid as uuid_lib

from django.urls import reverse


class InterestArea(models.Model):
    title = models.CharField(max_length=120)
    create_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)  # Used to find the web
    uuid = models.UUIDField(db_index=True,
                            default=uuid_lib.uuid4,
                            editable=False)

    class Meta:
        verbose_name = 'Área de Interesse'
        verbose_name_plural = 'Áreas de Interesse'
        ordering = ['create_date', 'title']

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('interestarea:detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.uuid = uuid_lib.uuid4()
        super(InterestArea, self).save(*args, **kwargs)
