from django.db import models
from django.db.models import permalink
from django.template.defaultfilters import slugify


class Category(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(max_length=100, unique=True, editable=False)
    description = models.TextField()

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    @permalink
    def get_absolute_url(self):  # would be useful for templates
        return 'category_detail', None, {'category_slug': self.slug}


class Product(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(max_length=100, unique=True, editable=False)
    description = models.TextField()
    price = models.PositiveIntegerField()
    created_at = models.DateTimeField(
        auto_now_add=True)  # automatically set datetime to now when a product is first created
    modified_at = models.DateTimeField(auto_now=True)  # automatically set datetime to now when a product is saved
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # many-to-one relationship

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    @permalink
    def get_absolute_url(self):
        return 'product_detail', None, {'product_slug': self.slug, 'category_slug': self.category.slug}
