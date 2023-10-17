from django import forms
from .models import Employee

# creating a form
class EmployeeForm(forms.ModelForm):
    # create meta class
    class Meta:
        model = Employee
        fields = [
            "name",
            "age",
            "gender",
            "joining_date",
            "designation",
            "place",
            "contact_no",
            "education"
        ]
        
        
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'required': 'false'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'required': 'false'}),
            'gender': forms.Select(attrs={'class': 'form-control', 'required': 'false'}),
            'joining_date': forms.TextInput(attrs={'class': 'form-control', 'required': 'false'}),
            'designation': forms.TextInput(attrs={'class': 'form-control', 'required': 'false'}),
            'place': forms.TextInput(attrs={'class': 'form-control', 'required': 'false'}),
            'contact_no': forms.TextInput(attrs={'class': 'form-control', 'required': 'false'}),
            'education': forms.TextInput(attrs={'class': 'form-control', 'required': 'false'}),
        }
        