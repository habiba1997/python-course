from django.contrib import admin
# configure and customize my admin panel (get it by default don't need to create it from scratch)
from .models import Book

# Register your models here.
admin.site.register(Book)
