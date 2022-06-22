from django.shortcuts import render , redirect
from .models import User
from.models import Profile
from .forms import Login_Form , UpdateUserForm ,UserCreationForms,UpdateProfileForm
from django.contrib.auth import login,authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.


def doctors_list(request):
    doctors = User.objects.all()
    context = {'doctors':doctors}
    return render (request,'user/doctors_list.html',context)


def doctors_detail(request , slug):
    doctors_detail = Profile.objects.get(slug=slug)
    context = {'doctors_detail':doctors_detail}
    return render (request,'user/doctors_detail.html',context)


def user_login(request):
    if request.method == 'POST':
        form = Login_Form()
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate (request,username=username,password=password)
        if user is not None :
            login(request,user)
            return redirect ('accounts:doctors_list')
    else:
        form = Login_Form()        



    
    return render (request,'user/login.html',{'form':form})


@login_required
def my_profile (request):
    return render (request,'user/my_profile.html')


@login_required
def update_profile (request):
    user_form = UpdateUserForm(instance=request.user)
    profile_form = UpdateProfileForm(instance=request.user.profile)
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user) 
        profile_form = UpdateProfileForm(request.POST,request.FILES,instance=request.user.profile)
        if user_form.is_valid and profile_form.is_valid:
            user_form.save()
            profile_form.save()
            return redirect ('accounts:doctors_list')
    return render (
    request,'user/update_profile.html',
    {'user_form':user_form , 'profile_form':profile_form}
    )




def user_signup(request): 
    if request.method == 'POST':
        form = UserCreationForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('accounts:login')
    else:
        form = UserCreationForms()


    return render (request,'user/signup.html',
    {'form':form}
    )



def contact_us (request):
    return render (request,'user/contact.html')




