from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from bravo_admin.models import User, Admin 


@api_view(['POST', 'GET'])
@permission_classes([AllowAny, ])
def Login(request):
    try:
        print("request---",request.META['PATH_INFO'])
        # del request.session['token']
        request_path = request.META['PATH_INFO']
        admin = False
        user = False
        if request_path == '/admin/':
            admin = True
        else:
            user = True
        print("admin--user---",admin, user)
        # print( request.session['designation'] )
        if request.method == 'GET':
            print('login')
           
            if 'token' in request.session and 'designation' in request.session:
                if admin and request.session['designation'] == 'Admin':
                    return redirect('/admin/home')
                elif user and request.session['designation'] != 'Admin':
                    return redirect('home/')
                else:
                    print('something wrong')
            return render(request,'login.html')

        if request.method == 'POST':
            print('post login')
            print("data---",request.POST)
            token = request.headers.get('X-CSRFToken')
            print("token---",token)
            if token == None or token == '':
                    return Response(data='Somthing wrong',status=status.HTTP_400_BAD_REQUEST)
            email = request.POST['email']
            password = request.POST['password']
            if user:
                print("user")
                if User.objects.filter(email=email).exists():
                    print('if')
                    u = User.objects.get(email=email)
                    print(check_password(password,u.password))
                    if check_password(password,u.password):
                        print("check if")
                        print("u.device---",u.device)
                        device = u.device
                        print("device--before-",device)
                        device.append(token)
                        print("device after append---",device)
                        u.device = device
                        u.save()
                        print("u.device---",u.device)
                        request.session['designation'] = u.designation
                        request.session['email'] = u.email
                        request.session['token'] = u.device[-1]
                        msg = 'Success'
                        return Response(data=msg,status=status.HTTP_200_OK)
                    else:
                        return Response(data='Password Wrong',status=status.HTTP_400_BAD_REQUEST)

                else:
                    print('else')
                    return Response(data='This Email Does Not Exists',status=status.HTTP_400_BAD_REQUEST)
            
            elif admin:
                print('admin')
                if Admin.objects.filter(email=email).exists():
                    print('if')
                    ad = Admin.objects.get(email=email)
                    print(check_password(password,ad.password))
                    if check_password(password,ad.password):
                        print("check if")
                        print("token---",token)
                        print("ad.device---",ad.device)
                        device = ad.device
                        print("device--before-",device)
                        device.append(token)
                        print("device after append---",device)
                        ad.device = device
                        ad.save()
                        print("ad.device---",ad.device)
                        # ad.device = token
                        # ad.save()
                        print("ad.device---",ad.device)
                        request.session['designation'] = ad.designation
                        request.session['email'] = ad.email
                        request.session['token'] = ad.device[-1]
                        msg = 'Success'
                        return Response(data=msg,status=status.HTTP_200_OK)
                    else:
                        return Response(data='Password Wrong',status=status.HTTP_400_BAD_REQUEST)

                else:
                    print('else')
                    return Response(data='This Email Does Not Exists',status=status.HTTP_400_BAD_REQUEST)
    except Exception as error:
        print('error',error)
        return Response(data='Something Wrong!!',status=status.HTTP_400_BAD_REQUEST)
        