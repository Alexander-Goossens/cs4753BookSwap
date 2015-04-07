from django.shortcuts import render
from home.forms import UserForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
def index(request):
	return render(request, 'home/index.html')
@login_required	
def about(request):
    return render(request, 'home/about.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/home/')
            else:
                return HttpResponse("Your account is disabled!")
        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")
            
    else:
        return render(request, 'home/login.html', {})

def register(request):
	registered = False

	if request.method == 'POST':
		user_form = UserForm(data=request.POST)

		if user_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			registered = True
		else:
			print(user_form.errors)
	else:
		user_form = UserForm()

	return render(request, 'home/register.html', {'user_form': user_form, 'registered': registered})

@login_required
def user_logout(request): 
    logout(request)
    return HttpResponseRedirect('/home/')