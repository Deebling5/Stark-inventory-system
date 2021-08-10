from django.contrib import admin
from .models import Stock

from django.contrib import admin
from django.contrib.admin.models import LogEntry
admin.site.register(LogEntry)

admin.site.register(Stock)