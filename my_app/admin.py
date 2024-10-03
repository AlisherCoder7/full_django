from django.contrib import admin
from .models import Book

# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title','price','author','publish','created','updated')
    list_filter = ('publish','author')
    search_fields = ('title','body')
    ordering = ('-publish',)
