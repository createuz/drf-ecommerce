from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Product(models.Model):
    sale = models.IntegerField(null=True)
    title = models.CharField(max_length=100)
    price = models.FloatField()
    color = models.CharField(max_length=100)
    image1 = models.ImageField()
    image2 = models.ImageField(blank=True, null=True)
    image3 = models.ImageField(blank=True, null=True)
    image4 = models.ImageField(blank=True, null=True)
    image5 = models.ImageField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Detail(models.Model):
    sale = models.IntegerField(null=True)
    title = models.CharField(max_length=100)
    price = models.FloatField()
    category = models.CharField(max_length=100, null=True)
    color = models.CharField(max_length=100)
    image1 = models.ImageField()
    image2 = models.ImageField(blank=True, null=True)
    image3 = models.ImageField(blank=True, null=True)
    image4 = models.ImageField(blank=True, null=True)
    image5 = models.ImageField(blank=True, null=True)
    gos = models.IntegerField()

    def __str__(self):
        return self.sale
