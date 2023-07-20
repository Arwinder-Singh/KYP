from django.contrib import admin
from .models import Profile,Tag,Rate,AvgRating
# Register your models here.

admin.site.register(Profile)
admin.site.register(Tag)
admin.site.register(Rate)
admin.site.register(AvgRating)
