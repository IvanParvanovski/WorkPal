from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import FormView, TemplateView
from django.contrib.auth import logout, authenticate, login
from ..forms.sign_in_form import SignInForm
from ..forms.sign_up_form import SignUpFormProfile, SignUpFormUser


class SignUpView(TemplateView):
    form_class_user = SignUpFormUser
    form_class_profile = SignUpFormProfile
    template_name = 'accounts_app/sign_up.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_user'] = self.form_class_user()
        context['form_profile'] = self.form_class_profile()
        return context

    def post(self, request, *args, **kwargs):
        form_user = self.form_class_user(request.POST)
        form_profile = self.form_class_profile(request.POST, request.FILES)

        if form_user.is_valid() and form_profile.is_valid():
            return self.forms_valid(form_user, form_profile)
        else:
            return self.forms_invalid(form_user, form_profile)

    def forms_valid(self, form_user, form_profile):
        try:
            user = form_user.save()
            form_profile.save(user=user)

            login(self.request, user)

            return redirect('home')
        except Exception as e:
            if str(e) == 'Passwords do not match!':
                form_user.add_error('password', 'Passwords do not match!')
            return self.forms_invalid(form_user, form_profile)

    def forms_invalid(self, form_user, form_profile):
        return render(self.request, self.template_name, {'form_user': form_user, 'form_profile': form_profile})


class SignInView(FormView):
    template_name = 'accounts_app/sign_in.html'
    form_class = SignInForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = authenticate(self.request, email=email, password=password)

        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            form.add_error(None, 'Invalid email or password')
            return self.form_invalid(form)


@login_required
def sign_out_view(request):
    logout(request)
    return redirect(reverse('home'))
