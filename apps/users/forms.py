from django import forms
from .models import User
from django.contrib.auth.models import Group
from awecounting.utils.forms import HTML5BootstrapModelForm


class UserAdminForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'full_name', 'email', 'is_superuser', 'last_login', 'groups']


class GroupAdminForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'permissions']


# from allauth.account.forms import SignupForm
# 
# 
# class SignupForm(SignupForm):
#     full_name = forms.CharField(label='Full name')
# 
#     def save(self, request):
#         user = super(SignupForm, self).save(request)
#         user.full_name = self.cleaned_data['full_name']
#         user.save()
#         return user
# 
#     def signup(self, request, user):
#         user.full_name = self.cleaned_data['full_name']
#         user.save()


class UserForm(HTML5BootstrapModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput, label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Password (again)')

    def clean_username(self):
        data = self.cleaned_data
        try:
            user = User.objects.get(username=data['username'])
            if user == self.instance:
                return data['username']
        except User.DoesNotExist:
            return data['username']
        raise forms.ValidationError('This username is already taken.')

    def clean_email(self):
        data = self.cleaned_data
        try:
            user = User.objects.get(email=data['email'])
            if user == self.instance:
                return data['email']
        except User.DoesNotExist:
            return data['email']
        raise forms.ValidationError('User with this email address already exists.')

    def clean(self):
        data = self.cleaned_data
        if "password1" in data and "password2" in data and data["password1"] != data["password2"]:
            raise forms.ValidationError("Passwords don't match.")

    def save(self):
        data = self.cleaned_data
        user = User.objects.create_user(username=data['username'], email=data['email'], password=data['password1'])
        user.full_name = data['full_name']
        user.save()
        return user

    class Meta:
        model = User
        exclude = ('last_login', 'is_active', 'is_staff', 'is_superuser', 'groups', 'password')


class UserUpdateForm(UserForm):
    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        self.fields['password1'].required = False
        self.fields['password2'].required = False

    def save(self):
        data = self.cleaned_data
        user = self.instance
        user.username = data['username']
        user.email = data['email']
        if data['password1'] != '':
            user.set_password(data['password1'])
        user.full_name = data['full_name']
        user.save()
        return user
