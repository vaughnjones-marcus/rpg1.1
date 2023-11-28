from django.contrib import admin

# Register your models here.
from .models import User, Activity, ExperienceLog

admin.site.register(User)
admin.site.register(Activity)
admin.site.register(ExperienceLog)