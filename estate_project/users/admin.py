from django.contrib import admin
from .models import *

# admin.site.register(UserProfile)
# admin.site.register(AgentProfile)
# admin.site.register(User)

class ProfileInline(admin.StackedInline):
    model = UserProfile
class AgentInline(admin.StackedInline):
    model = AgentProfile
class UserAdmin(admin.ModelAdmin):      
    def get_inlines(self, request, obj=None):
        if obj is None:
            return super().get_inlines(request, obj)

        if obj.is_agent:
            return [AgentInline]
        else:
            return [ProfileInline]
admin.site.register(User,UserAdmin)
admin.site.register(UserProfile)
admin.site.register(AgentProfile)
admin.site.register(Apartments)