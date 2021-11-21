# Create your models here.
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify
from taggit.managers import TaggableManager

# User = get_user_model()


class BaseContent(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = TaggableManager()
    is_active = models.BooleanField(default=True)
    slug = models.SlugField()
    # Abstract Class'da class meta deyip abstract = True atamamız lazım.
    class Meta:
        abstract = True


class Post(BaseContent):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    content = RichTextField()
    image = models.ImageField(
        "Gorsel",
        upload_to="post_images",
        default="not_found.jpg",
        blank=True,
    )

    def __str__(self) -> str:
        return str(self.author)

    # SİGNAL KULLANARAK OLUŞTUR
    def save(self, *args, **kwargs) -> None:
        if not self.pk:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = "post"

        verbose_name_plural = "posts"


class Comment(models.Model):
    parent = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    content = RichTextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = "Yorum"
        verbose_name_plural = "Yorumlar"
        ordering = ["-created", "-updated"]

    # ordering ekle
