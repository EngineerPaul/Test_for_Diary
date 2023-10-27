from django.views.generic import TemplateView

from .models import Book


class CaseWhenPage(TemplateView):
    template_name = 'case_when/case_when.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header_title'] = 'Изменение нескольких сущностей БД ' \
                                  'с условиями CASE-WHEN'
        # self.del_books()
        # self.create_books()
        # self.change_books()
        # self.del_books()
        self.change_books_by_list()
        context['books'] = Book.objects.all()
        return context

    def create_books(self):  # numbers: 1 2 3
        Book.objects.create(
            title='Сказать жизни Да!',
            genre='Психология',
            number=1
        )
        Book.objects.create(
            title='Вспомнить все',
            genre='Биография',
            number=2
        )
        Book.objects.create(
            title='Просто делай! Делай просто!',
            genre='Саморазвитие',
            number=3
        )
        return True

    def del_books(self):
        books = Book.objects.all()
        for book in books:
            book.delete()
        return True

    def change_books(self):  # numbers: 3 0 3
        # передача аргументов вручную

        from django.db.models import Case, Value, When

        Book.objects.update(
            number=Case(
                When(genre='Психология', then=Value(3)),
                When(number=2, then=Value(0)),
                # When(number=3, then=Value(1)),
                default='number',
            ),
        )
        return True

    def change_books_by_list(self):  # numbers: 3 2 1
        # передача аргументов списком (при помощи кода)

        from django.db.models import Case, Value, When

        # список с начальными значениями numbers и новыми
        order_list = [
            (1, 3),
            (2, 2),
            (3, 1)
        ]

        # список экземпляров When, которые мы применил в Case sql-запросе
        update_list = []
        for i in range(len(order_list)):
            update_list.append(When(
                number=order_list[i][0],
                then=Value(order_list[i][1])
            ))

        # расскрываем список When при помощи представления списков *args
        Book.objects.update(
            number=Case(*update_list),
        )
        return True
