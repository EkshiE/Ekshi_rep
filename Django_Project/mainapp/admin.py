from django.contrib import admin

from .models import Group
from .models import Students

admin.site.register(Students)
admin.site.register(Group)
