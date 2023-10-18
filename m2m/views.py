from django.views.generic import TemplateView

from .models import Record, People, PeopleRecordsLink


class ManyToManyPage(TemplateView):
    template_name = 'm2m/m2m.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header_title'] = 'm2m связь с использованием промежуточной таблицы'

        # self.create_entities()  # создание сущностей
        # self.delete_entities()  # удаление сущностей

        context['records'] = Record.objects.prefetch_related('people')
        # в records_m2m ниже для получения связей для каждой сущности делается
        # свой sql-запрос
        context['records_m2m'] = []
        for record in context['records']:
            context['records_m2m'].append({
                'record_title': record.title,
                'record_m2m': record.people.all()
            })

        context['people'] = People.objects.prefetch_related('record')
        context['people_m2m'] = []
        for human in context['people']:
            context['people_m2m'].append({
                'people_name': human.name,
                'people_m2m': human.record.all()
            })

        context['people_record'] = PeopleRecordsLink.objects.select_related(
            'people', 'record').all()

        return context

    def create_entities(self):
        any_record_1 = Record.objects.create(title='Случайная запись 1')
        any_record_2 = Record.objects.create(title='Случайная запись 2')

        any_human_1 = People.objects.create(name='Tom')
        any_human_2 = People.objects.create(name='Alice')

        human_1_record_1 = PeopleRecordsLink.objects.create(
            people=any_human_1,
            record=any_record_1,
            color='red',
            assessment=5
        )
        human_2_record_1 = PeopleRecordsLink.objects.create(
            people=any_human_2,
            record=any_record_1,
            color='blue',
            assessment=4
        )
        human_1_record_2 = PeopleRecordsLink.objects.create(
            people=any_human_1,
            record=any_record_2,
            color='green',
            assessment=3
        )

    def delete_entities(self):
        Record.objects.all().delete()
        People.objects.all().delete()
