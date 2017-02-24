from django.db import models

# Create your models here.

# Three models:
# PhoneNumber
# EmployeeDirectory(PhoneNumber)
# CallLog

class PhoneNumber(models.Model):
	pass

class EmployeeDirectory(PhoneNumber):
	pass

class CallLog(models.Model):
	pass
