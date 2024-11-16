from django.contrib import admin
from .models import Question, Option, Vote


class OptionInline(admin.TabularInline):
    model = Option
    
class QuestionAdmin(admin.ModelAdmin):
    inlines = [OptionInline]
    list_display = ['text','options','creat_at','enabled']
    list_filter = ['enabled']
    search_fields = ['text']
    
    def options(self, obj):
        return obj.option_set.count()
    
class VoteAdmin(admin.ModelAdmin):
    list_display = ['option__question','option','creat_at']
    

admin.site.register(Question, QuestionAdmin)
admin.site.register(Vote)