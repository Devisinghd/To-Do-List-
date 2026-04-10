from django import forms
from .models import Jobs

class tasksForm(forms.ModelForm):
    class Meta:
        model = Jobs
        fields = ['task','description','time']
