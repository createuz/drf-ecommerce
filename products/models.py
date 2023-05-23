from django.db import models

from accounts.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    color = models.CharField(max_length=100)
    original_price = models.FloatField()
    discount = models.FloatField()
    main_image = models.ImageField(upload_to='product_images')
    image1 = models.ImageField(upload_to='product_images', blank=True)
    image2 = models.ImageField(upload_to='product_images', blank=True)
    image3 = models.ImageField(upload_to='product_images', blank=True)
    image4 = models.ImageField(upload_to='product_images', blank=True)
    image5 = models.ImageField(upload_to='product_images', blank=True)
    image6 = models.ImageField(upload_to='product_images', blank=True)
    image7 = models.ImageField(upload_to='product_images', blank=True)
    image8 = models.ImageField(upload_to='product_images', blank=True)
    image9 = models.ImageField(upload_to='product_images', blank=True)
    image10 = models.ImageField(upload_to='product_images', blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.product.title}"


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
