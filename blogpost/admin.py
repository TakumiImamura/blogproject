from django.contrib import admin
from .models import SampleModel, BlogModel   #管理画面に認識させる
admin.site.register(SampleModel)
admin.site.register(BlogModel)