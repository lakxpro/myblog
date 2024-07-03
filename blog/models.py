from django.conf import settings
from django.db import models
from PIL import Image
from pathlib import Path


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="tag")

    class Meta:
        verbose_name = "tag"
        verbose_name_plural = "tagy"

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name="titulek")
    content = models.TextField(verbose_name="obsah")
    full_image = models.ImageField(upload_to="articles/", verbose_name="obrázek")
    image_thumb = models.ImageField(upload_to="articles/thumbs/", blank=True)
    tags = models.ManyToManyField(Tag, through="ArticleTag", related_name="articles", verbose_name="tagy")

    class Meta:
        verbose_name = "článek"
        verbose_name_plural = "články"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.full_image and not self.image_thumb:
            self.image_thumb = self.make_thumbnail(self.full_image)
            super().save(*args, **kwargs)  # Save again to update the image_thumb field

    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert("RGB")  # Convert image to RGB mode
        img.thumbnail(size)

        thumb_name, thumb_extension = (
            Path(image.name).stem,
            Path(image.name).suffix.lower(),
        )
        thumb_filename = f"{thumb_name}_thumb{thumb_extension}"
        thumb_path = Path("articles/thumbs") / thumb_filename
        full_thumb_path = Path(settings.MEDIA_ROOT) / thumb_path

        # Ensure the directory exists
        full_thumb_path.parent.mkdir(parents=True, exist_ok=True)

        # Save the thumbnail to the media folder
        img.save(full_thumb_path)

        # Return the relative path to the thumbnail
        return str(thumb_path)

    def __str__(self):
        return self.title


class ArticleTag(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("article", "tag")

    def __str__(self):
        return f"{self.article.title} - {self.tag.name}"
