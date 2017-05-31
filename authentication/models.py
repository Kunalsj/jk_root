# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth import User

# Create your models here.

class Record(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	
	class Meta:
		abstract = True

class Client(Record, User):
	token = models.CharField(max_length=10)

"""base User model contains following fields:

username - required
password - required
first_name
last_name
email
groups
user_permissions
is_staff
is_active
is_superuser
last_login
date_joined

"""
	
class ClientRequest(Record):
	message = models.TextField()
	client = models.ForeignKey('Client')
	response = models.TextField(blank=True)