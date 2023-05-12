from django.shortcuts import render,redirect
from usersystem.forms import UserEssentialForm
from usersystem.models import User
from django.urls import reverse
from termsandconditions.models import UserTermsAndConditions, TermsAndConditions

# Create your views here.

def render_test(request):
    from datetime import datetime
    today = datetime.now()
    user = "Mateus"
    data = {
        'datetime':today,
        'other':user
    }
    return render(request,"usersystem/test.html",context=data)

def user_list(request):
    users = User.objects.filter(is_superuser=False,is_staff=False)
    return render(request,"usersystem/user_list.html",context={'users':users})


def user_form_test(request):
    if request.method == 'POST':
        userform = UserEssentialForm(request.POST)
        if userform.is_valid():
            new_user = userform.save(commit=False)
            new_user.save()
            #associar ao termo de referência vigente
            return redirect(reverse('user:user_list'))
    else:
         userform = UserEssentialForm()
    return render(request,"usersystem/user_form.html",context={'form':userform})


def render_base(request):
    return render(request,"base.html")
    
    
def register_theo(request):
    if request.method == 'POST':
        user_form = UserEssentialForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.save()
            #associar ao termo de referência vigente
            return redirect(reverse('user:login_theo'))
    else:
        user_form = UserEssentialForm()
    return render(request,"usersystem/register_theo.html", context={'form': user_form})

def login_theo(request):
    return render(request,"usersystem/login_theo.html")


def render_login(request):
    return render(request,"usersystem/mateus/login.html")


def render_register(request):
    #return render(request,"usersystem/mateus/register.html")
    if request.method == 'POST':
        userform = UserEssentialForm(request.POST)
        if userform.is_valid():
            new_user = userform.save(commit=False)
            new_user.save()
            #associar ao termo de referência vigente
            if(TermsAndConditions.get_active()):
                UserTermsAndConditions.objects.create(
                    user = new_user,
                    terms = TermsAndConditions.get_active()
                )
            return redirect(reverse('user:user_list'))
    else:
        userform = UserEssentialForm()
    return render(request,"usersystem/mateus/register_form_django.html",context={'form':userform})
