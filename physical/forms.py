from django import forms

from physical.models import physical

class FormPhysical(forms.ModelForm):

	class Meta:
		model = physical

		fields = [
			'user',
			'Physical1',
			'Physical2',
			'Physical3',
			'Physical4',
			'Physical5',
			'Physical6',
			'Physical7',
			'Physical8',
			'Physical9',
			'Physical10',
			
		]
		labels = {
			'user': 'Seleccione su usuario',
			'Physical1': '¿Significado de Física: ?',
			'Physical2': '¿Definición de vector?',
			'Physical3': 'Un avion vuela hacia el norte a 90m/s , un fuerte viento sopla hacia el oeste a razón de 72 k/m y desvia el rumbo. Hallar la velocidad del avión para un observador en la tierra',
			'Physical4': 'Definición de trayectoria: ',
			'Physical5': '¿Cual es el concepto de velocidad?',
			'Physical6': '¿Cual es el concepto de velocidad media?',
			'Physical7': '¿Cual es el concepto de velocidad instantánea?',
			'Physical8': 'Definición de aceleración:',
			'Physical9': 'Dadas las ecuaciones: x+6y=27 y 7x-3y=9 resolver x',
			'Physical10': 'Dadas las ecuaciones 3x-2y=-2 y 5x+8y',			
			
		}
		widgets = {
			'Physical1': forms.TextInput(attrs={'class':'form-control'}),
			'Physical2': forms.TextInput(attrs={'class':'form-control'}),
			'Physical3': forms.TextInput(attrs={'class':'form-control'}),
			'Physical4': forms.TextInput(attrs={'class':'form-control'}),
			'Physical5': forms.TextInput(attrs={'class':'form-control'}),
			'Physical6': forms.TextInput(attrs={'class':'form-control'}),
			'Physical7': forms.TextInput(attrs={'class':'form-control'}),
			'Physical8': forms.TextInput(attrs={'class':'form-control'}),
			'Physical9': forms.TextInput(attrs={'class':'form-control'}),
			'Physical10': forms.TextInput(attrs={'class':'form-control'}),
		}