from datetime import date
from model_bakery import baker
from cursos.models import Curso
import pytest

@pytest.fixture
def curso():
    curso = baker.make(
        Curso,
        titulo = 'python',
        data_do_curso = date.today(),
        carga_horaria = '40'
    )    

@pytest.mark.django_db
def test_str_deve_retornar_string_formatada():
    assert str(curso) == 'Python: 2023-09-05 - 40'

def __str__(self):
    return f'{self.titulo}: {self.data_do_curso} - {self.carga_horaria}'