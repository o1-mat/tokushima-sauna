from django.contrib import admin
from .models import Spa, Category
from .models import Favorite, Review

admin.site.register(Favorite)
admin.site.register(Spa)
admin.site.register(Category)
admin.site.register(Review)




