from django.utils.text import slugify
from django.db import models
from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(null=False,blank=True,unique=True,db_index=True, editable=False)


    def __str__(self):
        return self.name
    
    def save(self, *args, **kwarqs ):
        self.slug = slugify(self.name)
        return super().save(*args, **kwarqs)


class Blog(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="blogs")
    description = RichTextField()
    is_active = models.BooleanField(default=False)
    is_home = models.BooleanField(default=False)
    slug = models.SlugField(null=True, blank=True,unique=True,db_index=True, editable=False)
    categories = models.ManyToManyField(Category,blank=True)
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwarqs ):
        self.slug = slugify(self.title)
        return super().save(*args, **kwarqs)
