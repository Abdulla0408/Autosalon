from django.db import models

# Create your models here.


class BrandCategory(models.Model):
    title = models.CharField(max_length=255, verbose_name="Kategoriya", unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Brand(models.Model):
    title = models.CharField(max_length=255, verbose_name="Car name")
    content = models.TextField(blank=True, null=True, verbose_name="Car info")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Enter time the car")
    updated = models.DateTimeField(auto_now=True, verbose_name="Edit time")
    published = models.BooleanField(default=True, verbose_name="Out to site")
    category = models.ForeignKey(BrandCategory, on_delete=models.CASCADE, verbose_name="Category")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'
        ordering = ('-pk',)

# ------------------------------------------------------------------------------------------


class ColorCategory(models.Model):
    title = models.CharField(max_length=255, verbose_name="Category", unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Color(models.Model):
    title = models.CharField(max_length=255, verbose_name="Car name")
    content = models.TextField(blank=True, null=True, verbose_name="Car info")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Enter time the car")
    updated = models.DateTimeField(auto_now=True, verbose_name="Edit time")
    published = models.BooleanField(default=True, verbose_name="Out to site")
    category = models.ForeignKey(ColorCategory, on_delete=models.CASCADE, verbose_name="Category")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Color'
        verbose_name_plural = 'Colors'
        ordering = ('-pk',)

# ------------------------------------------------------------------------------------------


class CarCategory(models.Model):
    title = models.CharField(max_length=255, verbose_name="Category", unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Car(models.Model):
    title = models.CharField(max_length=255, verbose_name="Car name")
    content = models.TextField(blank=True, null=True, verbose_name="Car info")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Enter time the car")
    updated = models.DateTimeField(auto_now=True, verbose_name="Edit time")
    published = models.BooleanField(default=True, verbose_name="Out to site")
    category = models.ForeignKey(CarCategory, on_delete=models.CASCADE, verbose_name="Category")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'
        ordering = ('-pk',)