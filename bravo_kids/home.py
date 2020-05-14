from django.shortcuts import render, redirect
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from bravo_admin.models import User, Admin, Tutorial


@api_view(['GET','POST'])
@permission_classes([AllowAny, ])
def Home(request):
    try:
        designation = request.session['designation']
        email = request.session['email']
        token = request.session['token']

        if designation == 'Admin':
            print("admin")
            if Admin.objects.filter(email=email,designation=designation).exists():
                print("if 1")
                admin_data = Admin.objects.get(email=email,designation=designation)
                print("admin_data---",admin_data)
                print("admin_data.device---",admin_data.device)
                print("token---",token)
                if token in admin_data.device:
                    print("if 2")
                    user_data = User.objects.all()
                    return render(request,'home.html',context={'user':admin_data,'user_data':user_data})
                # else:
                #     return redirect('/admin/')
        else:
            print("other")
            if User.objects.filter(email=email,designation=designation).exists():
                user_data = User.objects.get(email=email,designation=designation)
                user_data1 = User.objects.all()
                
                if token in user_data.device:
                    if user_data.designation == 'Student' or user_data.designation == 'Teacher':
                        tutorials = Tutorial.objects.filter(Student=user_data)
                        print("user_data---",user_data)
                        print("tutorials----",tutorials)
                        tutorials1 = Tutorial.objects.filter(Teacher=user_data.id)
                        print("tutorials1----",tutorials1)
                        return render(request,'home.html',context={'user':user_data,'tutorials':tutorials,'tutorials1':tutorials1,'user_data':user_data1})
                    return render(request,'home.html',context={'user':user_data,'user_data':user_data1})
    except Exception as error:
        print("Exception in home---",error)
        user_data1 = User.objects.all()
        return render(request,'home.html',context={'user_data':user_data1})