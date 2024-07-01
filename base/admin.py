from django.contrib import admin
from .models import *

class LearningOutcomesInline(admin.TabularInline):
    model = LEARNING_OUTCOMES

class VideoInline(admin.TabularInline):
    model = Video

class CourseAdmin(admin.ModelAdmin):
    inlines = [LearningOutcomesInline, VideoInline]

admin.site.register(Contact_us)
admin.site.register(Categories)
admin.site.register(Author)
admin.site.register(Internships, CourseAdmin)
admin.site.register(LEARNING_OUTCOMES)
admin.site.register(UserInternship)
admin.site.register(Lesson)
admin.site.register(Video)
