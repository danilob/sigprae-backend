from django.db import models

import uuid as uuid_lib

from django.urls import reverse

from apps.interestarea.models import InterestArea
class Subject(models.Model):
    description = models.CharField(max_length=220)
    create_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)  # Used to find the web
    interestareas = models.ManyToManyField(InterestArea, related_name='subjects', blank=False)
    uuid = models.UUIDField(db_index=True,
                            default=uuid_lib.uuid4,
                            editable=False)

    class Meta:
        verbose_name = 'Assunto'
        verbose_name_plural = 'Assuntos'
        ordering = ['create_date', 'description']

    def __str__(self):
        return self.description

    # def get_absolute_url(self):
    #     return reverse('Subject:detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.uuid = uuid_lib.uuid4()
        super(Subject, self).save(*args, **kwargs)
