# urls student


from django.urls import path
from student.views import displayAllStudents,test,student_details

# url resolver (main App )
urlpatterns = [
    path('', displayAllStudents),
    path('test',test),
    path('<int:id>',student_details,name="student_info"),
]
