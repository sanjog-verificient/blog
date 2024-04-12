from django.contrib import admin

# Register your models here.
from blogapp.models import Post

admin.site.register(Post)