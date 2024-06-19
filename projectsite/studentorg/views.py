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
from django.db import connection
from django.http import JsonResponse
from datetime import datetime
from django.db.models import Count
from calendar import month_abbr
from django.db import models    


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
    


class ChartView(ListView):
    template_name = 'chart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self, *args, **kwargs):
        pass


def StudentCountByProgram(request):
    # Fetching student counts per program
    program_counts = Student.objects.values('program__prog_name').annotate(count=Count('program')).order_by('-count')

    # Extracting labels (program names) and counts
    labels = [item['program__prog_name'] for item in program_counts]
    counts = [item['count'] for item in program_counts]

    data = {
        'labels': labels,
        'counts': counts,
    }
    return JsonResponse(data)


def OrganizationGraphData(request):
    # Query to get the count of organizations grouped by the college's name
    organizations = Organization.objects.values('college__college_name').annotate(count=Count('id')).order_by('college__college_name')
    
    # Prepare the data for the graph
    labels = [org['college__college_name'] if org['college__college_name'] else 'No College' for org in organizations]
    counts = [org['count'] for org in organizations]
    
    data = {
        'labels': labels,
        'counts': counts,
    }
    
    return JsonResponse(data)


def chart_students(request):
    program_counts = Program.objects.annotate(student_count=models.Count('student'))
    labels = [program.prog_name for program in program_counts]
    counts = [program.student_count for program in program_counts]
    return JsonResponse({'labels': labels, 'counts': counts})


def chart_org_members(request):
    org_counts = Organization.objects.annotate(member_count=models.Count('orgmember'))
    labels = [org.name for org in org_counts]
    counts = [org.member_count for org in org_counts]
    return JsonResponse({'labels': labels, 'counts': counts})


def chart_colleges(request):
    # Query the database to get data for the college pie chart
    # For example, let's say you want to count the number of students per college
    college_counts = College.objects.annotate(student_count=models.Count('program__student'))
    labels = [college.college_name for college in college_counts]
    counts = [college.student_count for college in college_counts]
    
    # Return the data as JSON response with a unique name
    return JsonResponse({'college_labels': labels, 'college_counts': counts})