from . import models
from django.contrib.auth import login
from django.contrib.auth.models import User
import pdb



def createuser(name,email,password):
	try:
		user = User.objects.create_user(username=name,email=email,password=password,is_superuser=False)

		if user:
			user.save()
			print(user)
			return user

	except Exception as exp:
		print(exp)
		return {'error':exp}



def deleteuser(username):
	try:
		user = User.objects.filter(id=username)
		user.delete()
		print(user)
		return user
	except Exception as exp:
		print(exp)
		return {'error':exp}


def check_if_user_exist(email):
	try:
		user = User.objects.filter(email=email).values()
		print(user)
		if user:
			return ({'error':"already exist"})
		else:
			return False


	except Exception as exp:
		print(exp)
		return ({'error':exp})




def get_org_id(org_name):
	try:
		pdb.set_trace()

		org_id=models.Org.objects.filter(org_name=org_name)[0].org_id
		print(org_id)
		return org_id

	except Exception as e:
		print(e)
		return({'error':e})

def get_orgs():
	try:
		org_list = models.Org.objects.all().values("org_name")
		if org_list:
			print(org_list)
			return org_list


	except Exception as e:
		print(e)
		return({'error':e})