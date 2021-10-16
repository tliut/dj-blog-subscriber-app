from django.shortcuts import render
from .models import SubscribersTable
from .forms import MyForm
from datetime import datetime



def home(request):
	return render(request, 'home.html')


def subscribe(request):
	form = MyForm()
	if request.method == 'POST':
		form = MyForm(request.POST)
		if form.is_valid():
			subscriber = SubscribersTable(
				firstname=form.cleaned_data['firstname'],
				email=form.cleaned_data['email'],
				created_on=datetime.today().strftime('%Y-%m-%d %H:%M:%S')
			)
			subscriber.save()
		else:
			return render(request,  'subscribe.html', {'form': form, 'error': 'Bad data entry.'})
		return render(request, 'subscribe.html', {'form': MyForm()})
	return render(request, 'subscribe.html', {'form': form})




