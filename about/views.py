from django.views.generic.base import TemplateView


class AboutAuthorView(TemplateView):
    template_name = 'about/default.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Об авторе'
        context['text'] = 'Меня зовут Олег Завитаев и я разработчик'
        return context


class AboutTechView(TemplateView):
    template_name = 'about/default.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Об использованных технологиях'
        context['text'] = 'Python, Django, Postgres, NGINX, Docker, Docker-compose, Github Actions'
        return context
