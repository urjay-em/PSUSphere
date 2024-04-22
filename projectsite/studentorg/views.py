from django.shortcuts import render
from django.views.generic.list import ListView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from studentorg.models import Organization, OrgMember, Student, College, Program
from studentorg.forms import OrganizationForm, OrgMemberForm, StudentForm, CollegeForm, ProgramForm
from django.urls import reverse_lazy
from typing import Any
from django.db.models.query import QuerySet
from django.db.models import Q
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


@method_decorator(login_required, name='dispatch')

class HomePageView(ListView):
    model = Organization
    context_object_name = 'home'
    template_name = 'home.html'

class OrganizationList(ListView):
    model = Organization
    context_object_name = 'organization'
    template_name = 'org_list.html'
    paginate_by = 5
    
    def get_queryset(self, *args, **kwargs):
        qs = super(OrganizationList, self).get_queryset(*args, **kwargs)
        if self.request.GET.get("q") != None:
            query = self.request.GET.get('q')
            qs = qs.filter(Q(name__icontains=query) |
                           Q(description__icontains=query) | Q(college__college_name__icontains=query))
        return qs
    
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
    context_object_name = 'orgMember'
    template_name = 'orgMember_list.html'
    paginate_by = 5
    
    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q')
        
        if query:
            # Remove leading and trailing whitespace
            query = query.strip()
            
            # Check if the query contains a comma (indicating full name search)
            if "," in query:
                lastname, firstname = map(str.strip, query.split(",", 1))
                # Filter by both first name and last name
                qs = qs.filter(Q(student__firstname__icontains=firstname) &
                               Q(student__lastname__icontains=lastname))
            else:
                # Filter queryset by student's full name, first name, last name, program name, organization name, and date joined
                qs = qs.filter(Q(student__lastname__icontains=query) |
                               Q(student__firstname__icontains=query) |
                               Q(student__program__prog_name__icontains=query) | 
                               Q(organization__name__icontains=query) | 
                               Q(date_joined__icontains=query))
                
        return qs




    
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
    context_object_name = 'student'
    template_name = 'student_list.html'
    paginate_by = 5
    
    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q')
        
        if query:
            query = query.strip()  # Remove leading and trailing whitespace
            
            if "," in query:
                lastname, firstname = map(str.strip, query.split(",", 1))
                qs = qs.filter(Q(lastname__icontains=lastname) &
                            Q(firstname__icontains=firstname))
            else:
                qs = qs.filter(Q(student_id__icontains=query) |
                            Q(lastname__icontains=query) |
                            Q(firstname__icontains=query) |
                            Q(middlename__icontains=query) |
                            Q(program__prog_name__icontains=query))
                
        return qs

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'student_add.html'
    success_url = reverse_lazy('student-list')
    
class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'student_edit.html'
    success_url = reverse_lazy('student-list')
    
class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'student_del.html'
    success_url = reverse_lazy('student-list')
    
    
    
    
    
    
    
class CollegeList(ListView):
    model = College
    context_object_name = 'College'
    template_name = 'college_list.html'
    paginate_by = 5
    
    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q')
        
        if query:
            query = query.strip()  # Remove leading and trailing whitespace
            qs = qs.filter(Q(college_name__icontains=query))
        
        return qs
            
    

class CollegeCreateView(CreateView):
    model = College
    form_class = CollegeForm
    template_name = 'college_add.html'
    success_url = reverse_lazy('college-list')
    
class CollegeUpdateView(UpdateView):
    model = College
    form_class = CollegeForm
    template_name = 'college_edit.html'
    success_url = reverse_lazy('college-list')
    
class CollegeDeleteView(DeleteView):
    model = College
    template_name = 'college_del.html'
    success_url = reverse_lazy('college-list')
    
    
    
    
    
class ProgramList(ListView):
    model = Program
    context_object_name = 'Program'
    template_name = 'program_list.html'
    paginate_by = 5
    
    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q')
        
        if query:
            query = query.strip()  # Remove leading and trailing whitespace
            qs = qs.filter(Q(prog_name__icontains=query) | Q(college__college_name__icontains=query))
        
        return qs

class ProgramCreateView(CreateView):
    model = Program
    form_class = ProgramForm
    template_name = 'program_add.html'
    success_url = reverse_lazy('program-list')
    
class ProgramUpdateView(UpdateView):
    model = Program
    form_class = ProgramForm
    template_name = 'program_edit.html'
    success_url = reverse_lazy('program-list')
    
class ProgramDeleteView(DeleteView):
    model = Program
    template_name = 'program_del.html'
    success_url = reverse_lazy('program-list')