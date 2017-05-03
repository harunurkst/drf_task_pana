from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import DivisionSerializer, DistrictSerializer, ThanaSerializer
from .models import Divisions, Districts, Thana


class DivisionsList(APIView):
    def get(self,request,format=None):
        div = Divisions.objects.all()
        serializer = DivisionSerializer(div, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DivisionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DistrictsList(APIView):
    def get(self,request,format=None):
        dist = Districts.objects.all()
        serializer = DistrictSerializer(dist, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DistrictSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ThanaList(APIView):
    def get(self, reqeust, format=None):
        thanas = Thana.objects.all()
        serializer = ThanaSerializer(thanas, many=True)
        return Response(serializer.data)

    def post(self,request, format=None):
        serializer = ThanaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


