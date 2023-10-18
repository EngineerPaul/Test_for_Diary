from django.views.generic import TemplateView


class SassPage(TemplateView):
    template_name = 'sass/sass.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header_title'] = 'Использование SASS/SCSS'
        return context
