"""
URL configuration for projectsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from studentorg.views import HomePageView, OrganizationList, OrganizationCreateView, OrganizationUpdateView, OrganizationDeleteView, OrgMemberList,  OrgMemberCreateView, OrgMemberUpdateView, OrgMemberDeleteView, StudentList, StudentCreateView, StudentUpdateView, StudentDeleteView, CollegeList, CollegeCreateView, CollegeUpdateView, CollegeDeleteView, ProgramList, ProgramCreateView, ProgramUpdateView, ProgramDeleteView                     
from studentorg import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.HomePageView.as_view(), name='home'),
    path('organization_list', OrganizationList.as_view(), name='organization-list'),
    path('organization_list/add', OrganizationCreateView.as_view(), name='organization-add'),
    path('organization_list/<pk>', OrganizationUpdateView.as_view(), name='organization-update'),
    path('organization_list/<pk>/delete', OrganizationDeleteView.as_view(), name='organization-delete'),
    re_path(r'^login/$', auth_views.LoginView.as_view(template_name='login'), name='login'),
    re_path(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    

   
    path('orgMemberList', OrgMemberList.as_view(), name='orgMember-list'),
    path('orgMemberList/add', OrgMemberCreateView.as_view(), name='orgMember-add'),
    path('orgMemberList/<pk>', OrgMemberUpdateView.as_view(), name='orgMember-update'),
    path('orgMemberList/<pk>/delete', OrgMemberDeleteView.as_view(), name='orgMember-delete'),



    path('studentList', StudentList.as_view(), name='Student-list'),
    path('studentList/add', StudentCreateView.as_view(), name='student-add'),
    path('orgMemberList/<pk>', StudentUpdateView.as_view(), name='student-update'),
    path('orgMemberList/<pk>/delete', StudentDeleteView.as_view(), name='student-delete'),
    
    
    path('collegeList', CollegeList.as_view(), name='college-list'),
    path('collegeList/add', CollegeCreateView.as_view(), name='college-add'),
    path('collegeList/<pk>', CollegeUpdateView.as_view(), name='college-update'),
    path('collegeList/<pk>/delete', CollegeDeleteView.as_view(), name='college-delete'),
    
    path('programList', ProgramList.as_view(), name='program-list'),
    path('programList/add', ProgramCreateView.as_view(), name='program-add'),
    path('programList/<pk>', ProgramUpdateView.as_view(), name='program-update'),
    path('programList/<pk>/delete', ProgramDeleteView.as_view(), name='program-delete'),
    
    
    
    re_path(r'^login/$', auth_views.LoginView.as_view(template_name='login'), name='login'),
    re_path(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
]


