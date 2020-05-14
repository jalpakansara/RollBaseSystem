from django.shortcuts import render, redirect
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from bravo_admin.models import User, Admin


@api_view(['GET'])
@permission_classes([AllowAny, ])
def Logout(request):
    try:
        print('logout')
        email = request.session['email']
        token = request.session['token']
        print("token--",token)
        designation = request.session['designation']
        if designation == 'Admin':
            u = Admin.objects.filter(email=email)
        else:
            u = User.objects.filter(email=email)

        if u:
            del request.session['email']
            del request.session['token']
            del request.session['designation']

            if designation == 'Admin':
                print('if')
                uObj = Admin.objects.get(email=email)
                if token in uObj.device:
                    print('if 2')
                    # for d in uObj.device:
                    #     if d == 'token':
                    aa = [del_token for del_token in uObj.device if del_token == token]
                    print('aa---',aa)
                    uObj.device.remove(aa[0])
                    uObj.save()
                return redirect('/admin/')
            else:
                uObj = User.objects.get(email=email)
                if token in uObj.device:
                    print('if 2')
                    # for d in uObj.device:
                    #     if d == 'token':
                    aa = [del_token for del_token in uObj.device if del_token == token]
                    print('aa---',aa)
                    uObj.device.remove(aa[0])
                    uObj.save()
                return redirect('/')
    except Exception as e:
        print('e',e)
        return redirect('/')