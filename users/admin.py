from django.contrib import admin
from .models import User, CheckCode

admin.site.register(User)
admin.site.register(CheckCode)