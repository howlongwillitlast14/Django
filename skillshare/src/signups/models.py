from django.db import models

# Create your models here.
class SignUp(models.Model):
	first_name = models.CharField(max_length=120, null=True, blank=True)
	last_name = models.CharField(max_length=120, null=True, blank=True)
	email = models.EmailField()#null=False, blank=False
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)#autonowadd when itis created make timestamp autonow when it is updated make timestamp(iwantnot)	
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return self.email

