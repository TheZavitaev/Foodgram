from django.views.generic.base import TemplateView


class AboutAuthorView(TemplateView):
    template_name = 'about/default.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Об авторе'
        context['text'] = 'Меня зовут Олег Завитаев и я выпускник 4 когорты ' \
                          'Яндекс.Практикума по специальности ' \
                          'Python-разработчик. ' \
                          'Мой телеграм: @thezavitaev, ' \
                          'github: https://github.com/TheZavitaev/'
        return context


class AboutTechView(TemplateView):
    template_name = 'about/default.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Об использованных технологиях'
        context['text'] = 'В данном проекте были использован следующий ' \
                          'технологический стек: ' \
                          'Python, Django, Postgres, NGINX, Docker, ' \
                          'Docker-compose, Github Actions. ' \
                          'Исходный код проекта размещен по адресу ' \
                          'https://github.com/TheZavitaev/foodgram-project'
        return context
