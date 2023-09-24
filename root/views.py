from django.views.generic import TemplateView


class Homepage(TemplateView):
    template_name = "root/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header_title'] = 'Перечень тестовых приложений'
        return context
