from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.views.generic import CreateView

from users.forms import CreationForm


class SignUp(CreateView):
    form_class = CreationForm
    success_url = '/accounts/login/'
    template_name = 'sign_up.html'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            user = form.save()
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
            )
            login(request, user)
            return redirect('recipe_list')
        return render(request, 'sign_up.html', {'form': form})
