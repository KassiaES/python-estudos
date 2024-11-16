from django.contrib import admin
from .models import Question, Option


#class AuthorAdmin(admin.ModelAdmin):
#    pass


admin.site.register(Question)
admin.site.register(Option)