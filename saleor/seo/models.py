from django.core.validators import MaxLengthValidator
from django.db import models

from ckeditor_uploader.fields import RichTextUploadingField


class SeoModel(models.Model):
    seo_title = models.CharField(
        max_length=70, blank=True, null=True, validators=[MaxLengthValidator(70)]
    )
    seo_description = models.CharField(
        max_length=300, blank=True, null=True, validators=[MaxLengthValidator(300)]
    )

    class Meta:
        abstract = True


class SeoModelTranslation(models.Model):
    seo_title = models.CharField(
        max_length=70, blank=True, null=True, validators=[MaxLengthValidator(70)]
    )
    seo_description = models.CharField(
        max_length=300, blank=True, null=True, validators=[MaxLengthValidator(300)]
    )

    class Meta:
        abstract = True


class Blog(models.Model):
    meta_robots = models.CharField(max_length=100, blank=True, null=True)
    meta_revisit = models.CharField(max_length=100, blank=True, null=True)
    meta_language = models.CharField(max_length=100, blank=True, null=True)
    meta_rating = models.CharField(max_length=100, blank=True, null=True)
    meta_copyright = models.CharField(max_length=100, blank=True, null=True)
    meta_google_site_verification = models.CharField(max_length=100, blank=True, null=True)
    meta_identifier = models.CharField(max_length=100, blank=True, null=True)
    meta_title = models.CharField(max_length=100, blank=True, null=True)
    meta_keywords = models.TextField(blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)

    title = models.CharField(max_length=100)
    news_content = RichTextUploadingField()
    short_description = models.TextField(null=True, blank=True,
                                         help_text='Short description shown on '
                                                   'blogs listing page')
    slug = models.CharField(null=True, blank=True, max_length=250)
    image = models.ImageField(blank=True, null=True)
    image_alt_text = models.CharField(max_length=15, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def to_dict(self):
        return {
            'meta_description': self.meta_description,
            'keywords': self.meta_keywords,
            'meta_title': self.meta_title,
            'identifier': self.meta_identifier,
            'google_site_verification': self.meta_google_site_verification,
            'copyright': self.meta_copyright,
            'rating': self.meta_rating,
            'language': self.meta_language,
            'revisit': self.meta_revisit,
            'robots': self.meta_robots,
            'short_description': self.short_description,
            'slug': self.slug,
            'title': self.title,
            'news_content': self.news_content,
            'image': self.image.path if self.image else None,
            'image_alt_text': self.image_alt_text,
            'created_at': self.created_at
        }

    def minimal_dict(self):
        return {
            'slug': self.slug,
            'title': self.title,
            'news_content': self.news_content,
            'image': self.image.path if self.image else None,
            'image_alt_text': self.image_alt_text,
            'created_at': self.created_at,
            'short_description': self.short_description,
        }

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'
