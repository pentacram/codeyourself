from django.contrib import admin
import nested_admin
from .models import *

admin.site.register(Questions)
admin.site.register(Answer)