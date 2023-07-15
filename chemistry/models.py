from django.db import models
from person.models import Persona

# Create your models here.

class Chemistry(models.Model):
	usuario_id = models.ForeignKey(Persona, null=True, blank=True, on_delete=models.CASCADE)
	Nombre = models.CharField(max_length=100, null=True)
	Chemistry1 = models.CharField(max_length=100, null=True)
	Chemistry2 = models.CharField(max_length=100, null=True)
	Chemistry3 = models.CharField(max_length=100, null=True)
	Chemistry4 = models.CharField(max_length=100, null=True)
	Chemistry5 = models.CharField(max_length=100, null=True)

	class Meta:
		verbose_name='chemistry'
		verbose_name_plural='chemistrys'

	def __str__(self):
		return '{}'.format(self.Nombre)