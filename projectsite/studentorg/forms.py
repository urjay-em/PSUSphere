from django.forms import ModelForm, TextInput, DateInput, Select
from django import forms
from .models import Organization, OrgMember, Student, College, Program

class OrganizationForm(ModelForm):
    class Meta:
        model = Organization
        fields = "__all__"
        
class OrgMemberForm(forms.ModelForm):
    date_joined = forms.DateField(label="date_joined",
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    class Meta:
        model = OrgMember
        fields = "__all__"
        


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        
        
        
class CollegeForm(ModelForm):
    class Meta:
        model = College
        fields = "__all__"
        
        
class ProgramForm(ModelForm):
    class Meta:
        model = Program
        fields = "__all__"