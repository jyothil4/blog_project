from django.shortcuts import render, redirect
from accounts.forms import CreateUserForm

# Signup code
def signUp(request):
	if request.user.is_authenticated:
		return redirect('post_list')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				return redirect('login')
		return render(request, 'registration/signup.html', {'form':form})
