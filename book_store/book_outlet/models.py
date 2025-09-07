from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100, null=True, blank=True)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", null=False)

    def get_absolute_url(self):
        return reverse("book_detail", args=[self.id, self.slug])
    
    #Override mehtod
    def save(self, *args, **kwargs):
        #Antes de agregar el registro se define el slug
        self.slug = slugify(self.title)
        
        #Heredar metodo save
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.rating})"