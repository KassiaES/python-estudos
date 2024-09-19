from django.contrib import admin
from cursos.models import Curso

# Register your models here.
@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_dispaly = ['titulo', 'nível', 'data_do_curso']
    search_field = ['titulo', 'nível']
    list_filter = ['data_do_curso']
