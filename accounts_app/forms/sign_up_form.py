from django import forms

from accounts_app.models import CustomUser
from accounts_app.models.profile import Profile
from services.generic.accounts_app.custom_user_service import CustomUserService
from services.generic.accounts_app.profile_service import ProfileService


class SignUpFormUser(forms.ModelForm):
    # Fields from CustomUser model
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
    rePassword = forms.CharField(widget=forms.PasswordInput, label='Confirm password')
    email = forms.EmailField()

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'password', 'rePassword', 'email']

    def save(self, commit=True):
        if self.cleaned_data['password'] != self.cleaned_data['rePassword']:
            raise Exception('Passwords do not match!')

        user = CustomUserService.create_custom_user(first_name=self.cleaned_data['first_name'],
                                                    last_name=self.cleaned_data['last_name'],
                                                    username=f"{self.cleaned_data['first_name']} {self.cleaned_data['last_name']}",
                                                    email=self.cleaned_data['email'],
                                                    password=self.cleaned_data['password'])

        # if commit:
        #     user.save()

        return user


class SignUpFormProfile(forms.ModelForm):
    # Fields from Profile model
    job_title = forms.CharField(max_length=50)
    description = forms.CharField(widget=forms.Textarea)
    image_path = forms.ImageField(required=False)

    class Meta:
        model = Profile
        fields = ['job_title', 'description', 'image_path']

    def save(self, user=None, commit=True):
        profile = ProfileService.create_profile(user=user,
                                                job_title=self.cleaned_data['job_title'],
                                                description=self.cleaned_data['description'],
                                                image_path=self.cleaned_data['image_path'])

        # if commit:
        #     profile.save()

        return profile
