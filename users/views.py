from django.core.mail import send_mail
from django.views.generic import CreateView

from users.forms import CreationForm

# TODO: Посмотри карена, там норм


class SignUp(CreateView):
    form_class = CreationForm
    success_url = "/accounts/login/"
    template_name = "registration/sign_up.html"

    def form_valid(self, form):
        email = form.cleaned_data['email']
        send_mail(
            'Добро пожаловать на Foodgram',
            'Вы успешно зарегистрировались на сайте Foodgram.',
            'foodgram-project@yandex.ru',
            [email],
            fail_silently=False,
        )
        return super().form_valid(form)
