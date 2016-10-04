from django.contrib import admin
from django.conf import settings
from main.models import *

class PrefaceAdmin(admin.ModelAdmin):
    list_display = ('admin_thumbnail', 'name')

    def admin_thumbnail(self, obj):
        return '<img src="%s%s" alt="" height="50">' % (settings.MEDIA_URL, obj.image)
    admin_thumbnail.allow_tags = True

class AboutAdmin(admin.ModelAdmin):
    list_display = ('admin_thumbnail', 'name')

    def admin_thumbnail(self, obj):
        return '<img src="%s%s" alt="" height="50">' % (settings.MEDIA_URL, obj.image)
    admin_thumbnail.allow_tags = True

class SkillAdmin(admin.ModelAdmin):
    pass

class GoalAdmin(admin.ModelAdmin):
    pass

class BenefitAdmin(admin.ModelAdmin):
    pass

class FeeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Preface, PrefaceAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Goal, GoalAdmin)
admin.site.register(Benefit, BenefitAdmin)
admin.site.register(Fee, FeeAdmin)
