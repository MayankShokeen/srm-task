from django.db import models
from django.contrib.auth.models import User
from . import managers
# Create your models here.
class Signup(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
	# name=models.CharField(max_length=100)
	# email = models.CharField(max_length=100)
	org_id =  models.IntegerField(default=1)
	objects = managers.Signup_manager()



class Org(models.Model):
	org_id = models.IntegerField(default=1,primary_key=True)
	org_name = models.CharField(max_length=100,default='')
	# objects = managers.Org_manager()


class Project(models.Model):
	org_id = models.IntegerField(default=1)

	project_id = models.AutoField(primary_key=True)
	project_name = models.CharField(max_length=100,default='')
	project_type = models.CharField(max_length=100,default='')
	assigned_to = models.CharField(max_length=100,default='')

# class Report(models.Model):
class Reports(models.Model):
	report_type = models.CharField(max_length=20,default='')
	project_id = models.IntegerField()
	session_starttime = models.TimeField()
	session_endtime = models.TimeField()
	comments = models.CharField(max_length=100)
	report_date = models.DateField()