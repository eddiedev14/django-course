from django.db import models
from django.utils.text import slugify

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"

class Tag(models.Model):
    caption = models.CharField(max_length=100)

    def __str__(self):
        return self.caption

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image_name = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    date = models.DateField(auto_now=False, auto_now_add=False)
    content = models.TextField()
    slug = models.SlugField(default="")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, *kwargs)

    def __str__(self):
        return f"{self.title} ({self.author.first_name} {self.author.last_name})"
    
class PostTag(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name="post_tags")

    def __str__(self):
        return f"{self.post.title} ({self.tag.caption})"
    class Meta:
        unique_together = ('post', 'tag')  # evita duplicados
