from django.db import models
import uuid

class Category(models.Model):
    name = models.CharField(max_length=120)
    create_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=150,unique=True,default="page-slug")

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = uuid.uuid4()
        super(Category, self).save(*args, **kwargs)

    def get_list_subjects(self):
        return self.subject_set.all() 



class Subject(models.Model):
    categories = models.ManyToManyField(Category)
    description = models.CharField(max_length=120)
    create_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=150,unique=True,default="page-slug")

    class Meta:
        verbose_name = 'Assunto'
        verbose_name_plural = 'Assuntos'
        ordering = ['description']

    def __str__(self):
        return self.description

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = uuid.uuid4()
        super(Subject, self).save(*args, **kwargs)

    #chamada via classe
    @staticmethod
    def count_subjects(): 
        return Subject.objects.all().count()

    #chamada é via objeto
    def get_list_categories(self):
        # list_categories = []
        # for category in self.categories.all():
        #     list_categories.append(category.name)
        list_categories = [category.name for category in self.categories.all()]
        return list_categories