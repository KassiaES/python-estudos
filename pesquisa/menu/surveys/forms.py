from django import forms
from .models import Question, Option


class QuestionForm(forms.ModelForm):
    option = forms.ModelChoiceField(empty_label="", required=True, queryset=None, widget=forms.RadioSelect)
    
    class Meta:
        model = Question
        fields = ['option']
        
    def __init__(self, *args, **kwargs):
        question = kwargs.pop('question', None)
        super().__init__(*args, **kwargs)
        self.fields['option'].queryset = question.option_set.all()
    