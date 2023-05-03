from django.core.exceptions import ValidationError
from django.forms import ModelForm
from polls.models import Schedule
from datetime import datetime
from django import forms



class ScheduleForm(forms.ModelForm):

    class Meta:
        model = Schedule
        fields = ['description', 'date']
        error_messages = {
            'description': {
                'required': ("Informe a descrição da tarefa completo."),
            },
            'date': {
                'required': ("Insira uma data válida."),
            }
        }

    def clean_description(self):
        description = self.cleaned_data['description']
        if not len(description) > 0:
            raise ValidationError('Necessário adicionar a descrição.')
        return description.strip().title()

    def clean_date(self):
        today = datetime.now().date()
        date = self.cleaned_data['date']
        if date.date() < today:
            raise ValidationError('A data da tarefa já passou')
        return date

    def clean(self):
        self.cleaned_data = super().clean()
        return self.cleaned_data
