from __future__ import unicode_literals

from django.db import models

class Users(models.Model):
	f_name = models.CharField(max_length = 255)
	l_name = models.CharField(max_length = 255)
	email = models.CharField(max_length = 255)
	password = models.CharField(max_length = 255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

class Messages(models.Model):
	message = models.TextField(max_length = 1000)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	user = models.ForeignKey(Users)

class Comments(models.Model):
	comment = models.TextField(max_length = 1000)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	user = models.ForeignKey(Users)
	message = models.ForeignKey(Messages)

	

