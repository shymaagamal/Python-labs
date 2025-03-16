from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

students=[
    {"name":"mina","age":20, "id":1},
    {"name":"shaimaa","age":40, "id":2},
    {"name":"Salem","age":30, "id":3},
    ]
def displayAllStudents(request):

    
    context={
        'student_html':students
    }
    return render(request,'student/all-students.html',context)

def test(request):
    return HttpResponse("test")


def student_details(request,id):
    
    result= list(filter(lambda std :std['id'] == id ,students))[0]
    context={
        'student_data':result
    }
    return render(request,'student/students.html',context)