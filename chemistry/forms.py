from django import forms

from chemistry.models import Chemistry

class RegistroFormChemistry(forms.ModelForm):

	class Meta:
		model = Chemistry

		fields = [
			'usuario_id',
			'Chemistry1',
			'Chemistry2',
			'Chemistry3',
			'Chemistry4',
			'Chemistry5',
			
		]
		labels = {
			'usuario_id': 'usuaario',
			'Chemistry1': '¿Como esta conformada la rama legislitiva de Colombia?',
			'Chemistry2': 'La tierra esta constituida por 3 elementos: ¿Cuales son?',
			'Chemistry3': 'La historia de la humanidad se compone enSelect la prehistoria (ágrafo) e historia (4000 a.c)',
			'Chemistry4': 'Las etapas de la prehistoria son: Edad de piedra y edad de los metales',
			'Chemistry5': 'La historia se divide en edad antigua (50000 a.c), edad media(1492-XV), edad moderna(XV-17889)',
			
		}
		widgets = {
			'Chemistry1': forms.TextInput(attrs={'class':'form-control'}),
			'Chemistry2': forms.TextInput(attrs={'class':'form-control'}),
			'Chemistry3': forms.TextInput(attrs={'class':'form-control'}),
			'Chemistry4': forms.TextInput(attrs={'class':'form-control'}),
			'Chemistry5': forms.TextInput(attrs={'class':'form-control'}),
		}