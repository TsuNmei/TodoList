from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    name = models.CharField(max_length=64, blank=True)
    email = models.EmailField(max_length=64, blank=True)
    avatar = models.URLField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    data = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    COLOR = (
        ('RED', 'red'),
        ('BLUE', 'blue'),
        ('GREEN', 'green'),
        ('YELLOW', 'yellow'),
        ('ORANGE', 'orange'),
        ('PURPLE', 'purple'),
        ('BLACK', 'black'),
        ('WHITE', 'white')
    )
    title = models.CharField(max_length=32)
    color = models.CharField(max_length=32, default='red', choices=COLOR)

    def __str__(self):
        return self.title


class Item(models.Model):
    PRIORITY_LEVEL = (
        ('HIGH', 'high'),
        ('MEDIUM', 'medium'),
        ('LOW', 'low')
    )
    creator = models.ForeignKey(UserProfile, related_name='items', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='categories', on_delete=models.CASCADE)
    title = models.CharField(max_length=32)
    description = models.TextField(max_length=64, blank=True)
    priority = models.CharField(max_length=32, default='medium', choices=PRIORITY_LEVEL)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'<{self.creator}> {self.title}'


admin.site.register(UserProfile)
admin.site.register(Item)
admin.site.register(Category)
