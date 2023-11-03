from django.contrib import admin
from.models import *
from django.utils.html import format_html
from django.utils.safestring import mark_safe
# Register your models here.

admin.site.register(Haber)
admin.site.register(Kategori)
admin.site.register(Biyografi)