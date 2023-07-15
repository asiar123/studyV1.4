from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import CreateView
from physical.models import physical
from physical.forms import FormPhysical
from django.urls import reverse_lazy


# Create your views here.

class añadirPhysical(PermissionRequiredMixin,CreateView):
	model = physical
	form_class = FormPhysical
	template_name = 'physical/new-physical.html'
	success_url = reverse_lazy('home')
	permission_required = {'usuario.permiso_admin'}