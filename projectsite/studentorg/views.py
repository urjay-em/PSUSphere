from django.shortcuts import render 
from django.views.generic.list import ListView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from studentorg.models import Organization, OrgMember, Student
from studentorg.forms import OrganizationForm, OrgMemberForm
from django.urls import reverse_lazy

class HomePageView(ListView):
    model = Organization
    context_object_name = 'home'
    template_name = 'home.html'

class OrganizationList(ListView):
    model = Organization
    context_object_name = 'organization'
    template_name = 'org_list.html'
    paginate_by = 5
    
class OrganizationCreateView(CreateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_add.html'
    success_url = reverse_lazy('organization-list')

class OrganizationUpdateView(UpdateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_edit.html'
    success_url = reverse_lazy('organization-list')
    
class OrganizationDeleteView(DeleteView):
    model = Organization
    template_name = 'org_del.html'
    success_url = reverse_lazy('organization-list')
    
    
    
    
    
    
    
class orgMemberhomePageView(ListView):
    model = OrgMember
    context_object_name = 'orgMemberhome'
    template_name = 'orgMemberhome.html'
    
class OrgMemberList(ListView):
    model = OrgMember
    context_object_name = 'OrgMember'
    template_name = 'orgMember_list.html'
    paginate_by = 5
    
class OrgMemberCreateView(CreateView):
    model = OrgMember
    form_class = OrgMemberForm
    template_name = 'orgMember_add.html'
    success_url = reverse_lazy('orgMember-list')
    
class OrgMemberUpdateView(UpdateView):
    model = OrgMember
    form_class = OrgMemberForm
    template_name = 'orgMember_edit.html'
    success_url = reverse_lazy('orgMember-list')
    
class OrgMemberDeleteView(DeleteView):
    model = OrgMember
    template_name = 'orgMember_del.html'
    success_url = reverse_lazy('orgMember-list')






class StudenthomePageView(ListView):
    model = Student
    context_object_name = 'studenthome'
    template_name = 'studenthome.html'
    
class StudentList(ListView):
    model = Student
    context_object_name = 'Student'
    template_name = 'student_list.html'
    paginate_by = 5
