from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from learn.models import Notice, Branch, profile, Question

# Register your models here.
class NoticeAdmin(ModelAdmin):
    list_display = ["subject","pub_date"]
    search_fields = ["subject"]
    list_filter = ["pub_date"]
    
admin.site.register(Notice, NoticeAdmin)

class BranchAdmin(ModelAdmin):
    list_display = ["name","hod"]
    
admin.site.register(Branch, BranchAdmin)
admin.site.register(profile)

class NoticeQuestion(ModelAdmin):
    list_display = ["subject","pub_date"]
    search_fields = ["subject"]
    list_filter = ["pub_date"]    
admin.site.register(Question, NoticeQuestion)
