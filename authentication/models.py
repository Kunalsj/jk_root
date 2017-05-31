# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Record(models.Model):
	time_ceated = models.DateTimeField(auto_now_add = True)
	last_modified = models.DateTimeField(auto_now = True)
	
	class Meta:
		abstract = True

class Client(Record):
	name = models.CharField(max_length = 50)
	email = models.EmailField()
	token = models.CharField(max_length = 20)

class Client_Request(Record):
	message = models.TextField()
	name = models.ForeignKey('Client')