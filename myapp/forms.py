from django import forms


class MyForm(forms.Form):
	firstname = forms.CharField(
		required=True,
		widget=forms.TextInput(
			attrs={'placeholder': 'FirstName', 'maxlength': '100'}
		),
	)
	email = forms.EmailField(
		required=True,
		widget=forms.TextInput(attrs={'placeholder': 'Email', 'maxlength': '100'}),
	)