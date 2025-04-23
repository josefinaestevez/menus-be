from django.utils.text import slugify


class SlugMixin:
    slug_source_field = 'name'

    def save(self, *args, **kwargs):
        if not self.slug:
            source = getattr(self, self.slug_source_field, None)
            if source:
                self.slug = slugify(source)
        super().save(*args, **kwargs)