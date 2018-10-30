from django.shortcuts import render,get_object_or_404

from django.template import loader

from .models import Student
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response
from quickstart.serializers import StudentSerializer


def index(request):
    student_list = Student.objects.order_by('-rate')
    template = loader.get_template('table/index.html')	
    context = {'student_list' : student_list}
    return render(request,'table/index.html',context)

def students(request, student_id):
	student = get_object_or_404(Student, pk=student_id)
	return render(request, 'table/detail.html', {'student': student})

# Create your views here.
