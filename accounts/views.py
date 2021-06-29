from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from contacts.models import Contact

# Create your views here.


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, "you are logged in..")
            return redirect('dashboard')
        else:
            messages.error(request, "invalid login credentials..")
            return redirect('login')

    return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, "Successfully logged out..")
        return redirect('home')
    return redirect('home')


def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, "username already exists..")
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, "email already exists..")
                    return redirect('register')
                else:
                    user = User.objects.create_user(
                        first_name=firstname, last_name=lastname, email=email, username=username, password=password)
                    # auth.login(request, user)
                    # messages.success(request, "you are logged in..")
                    # return redirect('dashboard')
                    #  above lines(35,36,37) are for auto login
                    user.save()
                    messages.success(
                        request, "you are registred successfully..")
                    return redirect('login')
        else:
            messages.error(request, "passwords do not match")
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')


@login_required(login_url='login')
def dashboard(request):
    user_inquiry = Contact.objects.order_by(
        '-create_date').filter(user_id=request.user.id)
    # count = Contact.objects.order_by('-create_date').filter(user_id=request.user.id).count()

    data = {
        'inquiries': user_inquiry,
    }
    return render(request, 'accounts/dashboard.html', data)
