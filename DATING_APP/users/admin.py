from django.contrib import admin
from .models import UserProfile
from .models import CustomUser
from .models import Interests

admin.site.register(Interests)

admin.site.register(CustomUser)

admin.site.register(UserProfile)


