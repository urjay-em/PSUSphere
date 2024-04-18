from django.forms import ModelForm, TextInput, DateInput, Select

from django import forms
from .models import Organization, OrgMember, Student

class OrganizationForm(ModelForm):
    class Meta:
        model = Organization
        fields = "__all__"
        
class OrgMemberForm(ModelForm):
    class Meta:
        model = OrgMember
        fields = "__all__"
        widgets = {
            'student': TextInput(attrs={'class': 'form-control'}),  
            'date_joined': DateInput(attrs={'type': 'date'}),
        }

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = "__all__"