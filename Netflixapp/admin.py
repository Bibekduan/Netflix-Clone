from django.contrib import admin
from .models import Profile,Movie,Video,CustonUser
# Register your models here.

admin.site.register(Profile)
admin.site.register(Movie)
admin.site.register(Video)
admin.site.register(CustonUser)