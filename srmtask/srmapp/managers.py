from django import forms
from django.db import models



class Signup_manager(models.Manager):
    def create_user(self,name,email,org_id):
    	user = self.create(user=user,org_id=org_id)
    	return user

