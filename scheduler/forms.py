from .models import DjangoJob, DjangoJobExecution
from django import forms



class DateForm(forms.Form):
    date = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        })
    )

class JobForm(forms.ModelForm):
    class Meta:
        model = DjangoJob
        fields = ["app_name", "next_run_time", "deploy_type"]
        widgets = {
            "deploy_type": forms.RadioSelect,
        }

class JobExecutionForm(forms.ModelForm):
    class Meta:
        model = DjangoJobExecution
        fields = "__all__"
