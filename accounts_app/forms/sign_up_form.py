from django import forms

from accounts_app.models.profile import Profile
from services.generic.accounts_app.custom_user_service import CustomUserService
from services.generic.accounts_app.profile_service import ProfileService


class SignUpForm(forms.ModelForm):
    # Fields from CustomUser model
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()

    # Fields from Profile model
    job_title = forms.CharField(max_length=50)
    description = forms.CharField(widget=forms.Textarea)
    image_path = forms.ImageField()

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'password', 'email', 'job_title', 'description', 'image_path']

    def save(self, commit=False):
        username = f"{self.cleaned_data['first_name']} {self.cleaned_data['last_name']}"
        user = CustomUserService.create_custom_user(username=username,
                                                    email=self.cleaned_data['email'],
                                                    password=self.cleaned_data['password'])

        profile = ProfileService.create_profile(user=user,
                                                job_title=self.cleaned_data['job_title'],
                                                description=self.cleaned_data['description'],
                                                image_path=self.cleaned_data['image_path'])

        if commit:
            user.save()
            profile.save()

        return profile
