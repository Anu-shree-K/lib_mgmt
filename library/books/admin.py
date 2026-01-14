from django.contrib import admin

# Register your models here.

from .models import BookCategory, Member

admin.site.register(BookCategory)
admin.site.register(Member)
