from django.shortcuts import render
from .models import StudentModel
from .serializers import studentSerializer
from django.http import JsonResponse,Http404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets

# Create your views here.


#Manual serialization
# def studentView(request):
#     student = StudentModel.objects.all()
#     student_list = list(student.values())
#     return JsonResponse(student_list,safe=False)

# @api_view(["GET","POST"])
# def studentView(request):
#     if request.method == "GET":
#         student = StudentModel.objects.all()
#         serializer = studentSerializer(student, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == "POST":
#         serializer = studentSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status= status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
#
#
#
# @api_view(["GET","PUT","DELETE"])
# def studentUpdateView(request,id):
#     try:
#         student = StudentModel.objects.get(id=id)
#     except student.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == "GET":
#         serializer = studentSerializer(student)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == "PUT":
#         serializer = studentSerializer(student,data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status= status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
#     elif request.method == "DELETE":
#          student.delete()
#          return Response(status=status.HTTP_410_GONE)
#
#


#Class Based views(CBV)

#
# class studentDataView(APIView):
#     def get(self,request):
#         student = StudentModel.objects.all()
#         serializer = studentSerializer(student,many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def post(self,request):
#         serializer = studentSerializer(data= request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class studentDataModifyView(APIView):
#       def get_object(self,pk):
#           try:
#               return StudentModel.objects.get(pk=pk)
#           except StudentModel.DoesNotExist:
#               raise Http404
#
#       def get(self,request,pk):
#           employee = self.get_object(pk)
#           serializer = studentSerializer(employee)
#           return Response(serializer.data, status=status.HTTP_302_FOUND)
#
#
#       def put(self,request,pk):
#           employee = self.get_object(pk)
#           serializer = studentSerializer(employee,data = request.data)
#           if serializer.is_valid():
#               serializer.save()
#               return Response(serializer.data, status=status.HTTP_201_CREATED)
#           return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
#       def delete(self,request,pk):
#           employee = self.get_object(pk)
#           employee.delete()
#           return Response(status=status.HTTP_200_OK)
#
#


#
# class studentDataView(mixins.ListModelMixin, mixins.CreateModelMixin ,generics.GenericAPIView):
#     queryset = StudentModel.objects.all()
#     serializer_class = studentSerializer
#     def get(self,request):
#         return self.list(request)
#
#     def post(self,request):
#         return self.create(request)
#

#
# class studentDataModifyView(mixins.UpdateModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
#     queryset = StudentModel.objects.all()
#     serializer_class = studentSerializer
#
#     def get(self,request,pk):
#         return self.retrieve(request,pk)
#
#     def put(self,request,pk):
#         return self.update(request,pk)
#
#     def delete(self,request,pk):
#         return self.destroy(request,pk)
#
#
#
#
# class studentDataView(generics.ListCreateAPIView):
#       queryset = StudentModel.objects.all()
#       serializer_class = studentSerializer
#
#
#
# class studentDataModifyView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = StudentModel.objects.all()
#     serializer_class = studentSerializer
#     lookup_field = "pk"
#
#
#
#
# class studentObjectInfoView(viewsets.ViewSet):
#     def list(self,request):
#         queryset= StudentModel.objects.all()
#         serializer = studentSerializer(queryset,many=True)
#         return Response(serializer.data)
#
#
#     def create(self,request):
#         serializer = studentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#
#
#     def retrieve(self,request,pk=None):
#         queryset = StudentModel.objects.get(pk=pk)
#         serializer = studentSerializer(queryset)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#



class studentObjectInfoView(viewsets.ModelViewSet):
       queryset = StudentModel.objects.all()
       serializer_class = studentSerializer



