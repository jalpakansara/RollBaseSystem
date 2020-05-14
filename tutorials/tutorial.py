from django.shortcuts import render, redirect
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from bravo_admin.models import User, Admin, Tutorial


@api_view(['POST'])
@permission_classes([AllowAny, ])
def Tutorial_add(request):
    try:
        print('Tutorial_add',request.data)
        students = request.POST['students']
        studentsList = eval(students)
        teacher = request.POST['teacher']
        room_no = request.POST['room_no']
        subject = request.POST['subject']
        # lead_assesment.learning_profile_answers.add(lQuerySet)
        # if User.objects.filter(email=email).exists():
        #     print('if')
        #     return Response(data='Email allready exists',status=status.HTTP_400_BAD_REQUEST)
        # else:
        #     print('else')
        tutoObj = Tutorial.objects.create(Teacher=teacher,room=room_no,subject=subject)
        print('tutoObj--',tutoObj)
        for s in studentsList:
            sobj = User.objects.get(id=s)
            tutoObj.Student.add(sobj)
        tutoObj.save()
        return Response(data='Successfully add tutorial.',status=status.HTTP_200_OK)
    except Exception as error:
        print('error',error)
        return Response(data='Somthing Wrong',status=status.HTTP_400_BAD_REQUEST)