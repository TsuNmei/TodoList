from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from revauth.models import BaseProfile


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=32)

    def __str__(self):
        return f'<{self.user}> {self.name}'


# class UserProfile(BaseProfile):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
#     name = models.CharField(max_length=32)


class Category(models.Model):
    """
    COLOR = (
        ('BLACK', 'BLACK'),
        ('DARK', 'DARK'),
        ('RED', 'RED'),
        ('BLUE', 'BLUE'),
        ('GREEN', 'GREEN'),
    )
    """
    creator = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=32)
    color = models.CharfField(max_length=32)
    # color = models.CharField(max_length=32, default='RED', choices=COLOR)
    
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


admin.site.register(UserProfile)
admin.site.register(Item)
admin.site.register(Category)
