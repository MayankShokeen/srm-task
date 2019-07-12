from django.shortcuts import render,redirect,render_to_response
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from . import db
from .  import models
import json
import pdb
from django.contrib import auth
import shutil
import os
# Create your views here.

def home(request):
	return render(request,"home.html",{})

def signup(request):
	return render(request,"signup.html",{})

def login(request):
	return render(request,"login.html",{})

@csrf_exempt
def save_user(request):
	if request.user.is_authenticated:
		return render(request,"upload.html",{})
	
	else:
		data=json.loads(request.body.decode('utf-8'))
		org_name=data.get('org_name')["org_name"]
		name=data.get('name')
		email=data.get('email')
		password=data.get('password')
		print(org_name)

		if(name and org_name and email and password):
			org_id=db.get_org_id(org_name)
			print(org_id)
			pdb.set_trace()
			user_exist=db.check_if_user_exist(email)
			if user_exist==False:
				signup = db.createuser(name,email,password)
				if type(signup) == dict:
					return JsonResponse({'status':'False','message':'User Exists'}, status=400)
				try:
					saving_user = models.Signup.objects.create_user(signup,org_id)
					saving_user.save()
				except Exception as exp:
					print(exp)
					return JsonResponse({'status':'false','message':'Please use unique details'}, status=400)
					print(signup.id)
					print(db.deleteuser(signup.id))
				if saving_user:
					return JsonResponse({"status":"True","message":"User successfully created"},status=200)
				else:
					return JsonResponse({"status":"False","message":"Error creating User"},status=400)
			
			else:
				return JsonResponse({"status":"False","message":"User already exist, try logging in"},status=400)

		
		else:
			return JsonResponse({"status":"False","message":"fill all the details"},status=400)




@csrf_exempt
def login_check(request):

	data=json.loads(request.body.decode('utf-8'))
	# pdb.set_trace()
	if not data:
		return JsonResponse({'status':'False','message':'No Data Received'}, status=400)
	org_id=data.get('org_id')
	email=data.get('email')
	password=data.get('password')
	user = auth.authenticate(email=email, password=password,org_id=org_id)
	print(user)
	auth.login(request, user)
	if not user:
		return JsonResponse({'status':'False','message':'Incorrect Id Or Password'}, status=400)
	else:
		return JsonResponse({'status':'True','message':'Logged In'},status=200)




@csrf_exempt
def logout(request):
	auth.logout(request)
	return render(request,"home.html",{})




def org_show(request):

        org_list = db.get_orgs()
        print(org_list)
        # pdb.set_trace()
        if not org_list:
            return JsonResponse({'status':'False','message':'no organization'}, status=400)

        print(org_list)
        return JsonResponse({'status':'true','message':list(org_list)}, status=200)




