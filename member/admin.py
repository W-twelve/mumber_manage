from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Grqx)
class GrqxAdmin(admin.ModelAdmin):
    list_display = ('id','QX')

@admin.register(models.Jbxx)
class JbxxAdmin(admin.ModelAdmin):
    list_display = ('xh','name','sex','age','yx','zy','jg','bm','zb')

