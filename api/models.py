from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=32)

    def __str__(self):
        return f'<{self.user}> {self.name}'


class Category(models.Model):
    creator = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=32)
    color = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.creator} -{self.title}"


class Item(models.Model):
    PRIORITY_LEVEL = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3')
    )
    creator = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='items')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categories')
    title = models.CharField(max_length=32)
    description = models.TextField(max_length=64, blank=True)
    priority = models.CharField(max_length=32, default='2', choices=PRIORITY_LEVEL)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'<ID:{self.pk}> {self.title}'


class ItemImage(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='images')
    name = models.CharField(max_length=32)
    image = models.ImageField(upload_to='items_img/')

    def __str__(self):
        return self.name


admin.site.register(UserProfile)
admin.site.register(Item)
admin.site.register(ItemImage)
admin.site.register(Category)
