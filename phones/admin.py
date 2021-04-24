from django.contrib import admin
from .models import Apple, Samsung, Xiaomi, Phone

admin.site.register(Phone)
admin.site.register(Apple)
admin.site.register(Samsung)
admin.site.register(Xiaomi)
