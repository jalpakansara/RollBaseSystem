from django.shortcuts import render, redirect
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from bravo_admin.models import User, Admin
from django.contrib.auth.hashers import make_password, check_password


@api_view(['POST'])
@permission_classes([AllowAny, ])
def Register(request):
    try:
        print('register',request.data)
        email = request.data['email']
        designation = request.data['designation']
        fname = request.data['fname']
        lname = request.data['lname']
        password = request.data['password']
        if User.objects.filter(email=email).exists():
            print('if')
            return Response(data='Email allready exists',status=status.HTTP_400_BAD_REQUEST)
        else:
            print('else')
            u = User.objects.create(first_name=fname,last_name=lname,email=email,password=make_password(password),designation=designation)
            print('u--',u)
            return Response(data='Successfully Created '+designation,status=status.HTTP_200_OK)
    except Exception as error:
        print('error',error)
        return Response(data='Somthing Wrong',status=status.HTTP_400_BAD_REQUEST)