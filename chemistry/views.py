from django.views.generic import CreateView
from chemistry.models import Chemistry
from chemistry.forms import RegistroFormChemistry
from django.urls import reverse_lazy

# Create your views here.

class añadirChemistry(CreateView):
	model = Chemistry
	template_name = 'chemistry/new-chemistry.html'
	form_class = RegistroFormChemistry
	success_url = reverse_lazy('physical')