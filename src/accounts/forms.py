
import email
from pyexpat import model
from django import forms
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class Login_Form(forms.ModelForm):
    username = forms.CharField(label='اسم المستخدم')
    password = forms.CharField(label='كلمة المرور',widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username','password')



class UpdateUserForm(forms.ModelForm):
    first_name = forms.CharField(label='الإسم الأول : ')
    last_name = forms.CharField(label='الإسم الأخير : ')
    email = forms.EmailField(label='البريد الإلكتروني : ')

    class Meta:
        model = User
        fields = ('first_name','last_name','email')


class UserCreationForms(UserCreationForm):
    username = forms.CharField(label='اسم المستخدم')
    first_name = forms.CharField(label='الإسم الأول : ')
    last_name = forms.CharField(label='الإسم الأخير : ')
    email = forms.EmailField(label='البريد الإلكتروني : ')
    password1 = forms.CharField(label='كلمة المرور',widget=forms.PasswordInput(),min_length=8)
    password2 = forms.CharField(label='تأكيد كلمة المرور',widget=forms.PasswordInput(),min_length=8)
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')        


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('name','who_i','price','subtitle','image','address','address_detail','phone_number','working_hours','wating_time','doctor','facebook','twitter','instagram','specialist_doctor')

