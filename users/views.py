from django.forms import model_to_dict
from django.shortcuts import render
from django.contrib.auth.hashers import make_password

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import CustomUser
from .serializers import CustomUserSerializer


class CustomUsersAPIView(APIView):
    def get(self, request):
        pk = request.GET.get('pk', '')

        if not pk:
            lst = CustomUser.objects.all()
            return Response({'users': CustomUserSerializer(lst, many=True).data})
        else:
            try:
                lst = CustomUser.objects.get(pk=pk)
                return Response({'user': CustomUserSerializer(lst).data})
            except:
                return Response({'error': 'Object does not exist.'})

    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'user': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Method PUT not allowed.'})

        try:
            instance = CustomUser.objects.get(pk=pk)
        except:
            return Response({'error': 'Object does not exist.'})

        serializer = CustomUserSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'post': serializer.data})

    def delete(self, *args, **kwargs):
        pk = kwargs.get('pk', None)
        print(pk)
        if not pk:
            return Response({'error': 'Method DELETE not allowed.'})

        try:
            CustomUser.objects.get(pk=pk).delete()
        except:
            return Response({'error': 'Object does not exist.'})

        return Response({'post': 'delete post with pk = ' + str(pk)})

    def patch(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)

        if not pk:
            return Response({'error': 'Method DELETE not allowed.'})

        try:
            instance = CustomUser.objects.get(pk=pk)
        except:
            return Response({'error': 'Object does not exist.'})

        serializer = CustomUserSerializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'post': serializer.data})
