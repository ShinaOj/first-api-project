from django.urls import path
from .views import StudentList, StudentDetails, StudentListView, StudentListCreateView, GraduatingStudent



urlpatterns=[
    path('students/', StudentList.as_view(), name='student_list'),
    path('student_list/', GraduatingStudent.as_view(), name='student'),
    path('students/<int:pk>/', StudentDetails.as_view(), name='student_detail')
    
]