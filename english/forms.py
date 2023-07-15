from django import forms

from english.models import English

from django.contrib.admin.widgets import AutocompleteSelect

class RegistroFormEnglish(forms.ModelForm):

	class Meta:
		model = English

		fields = [
			'usuario',
			'Nombre',
			'English1',
			'English2',
			'English3',
			'English4',
			'English5',
			'English6',
			'English7',
			'English8',
			'English9',
			'English10',
			'English11',
			
		]
		labels = {
			'usuario': forms.Select(attrs={'class':'form-control'}),
			'English1': '1.	VERB HAVE',
			'English2': '2. VERB LEARN',
			'English3': '3.	VERB START',
			'English4': '4.	VERB DISCOVER',
			'English5': '5.	VERB ESTABLISH',
			
		}
		widgets = {
			'English1': forms.TextInput(attrs={'class':'form-control'}),
			'English2': forms.TextInput(attrs={'class':'form-control'}),
			'English3': forms.TextInput(attrs={'class':'form-control'}),
			'English4': forms.TextInput(attrs={'class':'form-control'}),
			'English5': forms.TextInput(attrs={'class':'form-control'}),
		}