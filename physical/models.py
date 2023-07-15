from django.db import models
from user.models import Usuario

# Create your models here.

class physical(models.Model):
	user=models.ForeignKey(Usuario, null=True, blank=True, on_delete=models.CASCADE)
	Physical1 = models.CharField(max_length=100, null=True)
	Physical2 = models.CharField(max_length=100, null=True)
	Physical3 = models.CharField(max_length=100, null=True)
	Physical4 = models.CharField(max_length=100, null=True)
	Physical5 = models.CharField(max_length=100, null=True)
	Physical6 = models.CharField(max_length=100, null=True)
	Physical7 = models.CharField(max_length=100, null=True)
	Physical8 = models.CharField(max_length=100, null=True)
	Physical9 = models.CharField(max_length=100, null=True)
	Physical10 = models.CharField(max_length=100, null=True)

	class Meta:
		verbose_name='physical'
		verbose_name_plural='physicals'

	def __str__(self):
		return '{}'.format(self.user)