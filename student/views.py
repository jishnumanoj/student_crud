from django.shortcuts import render

from django.views.generic import View
from student.models import Student
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
# Create your views here.
from json import loads


@method_decorator(csrf_exempt,name='dispatch')
class StudentListCreateView(View):

    def get(self,request):

        qs = Student.objects.all().values()

        response_data = list(qs)

        return JsonResponse(response_data,safe=False)


    def post(self,request):

        json_data = request.body

        form_data = loads(json_data)

        Student.objects.create(
            name=form_data.get("name"),
            course=form_data.get("course"),
            college=form_data.get("college"),
            email=form_data.get("email")
        )

        response_data = {"message":"Student Created"}

        return JsonResponse(response_data)


@method_decorator(csrf_exempt,name='dispatch')
class StudentRetieveUpdateDeleteView(View):

    def get(self,request,pk=None):

        qs = Student.objects.filter(id=pk).values()

        respone_data = list(qs)

        return JsonResponse(respone_data,safe=False)

    def put(self,request,pk=None):

        json_data = request.body

        form_data = loads(json_data)

        Student.objects.filter(id=pk).update(
            name=form_data.get("name"),
            course=form_data.get("course")
        )

        response_data = {"message":"Student Updated"}

        return JsonResponse(response_data)