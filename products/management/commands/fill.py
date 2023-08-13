from django.core.management import BaseCommand
from products.models import Category, Product


# Класс для заполнения БД данными, с предварительной очисткой БД.
class Command(BaseCommand):
    def handle(self, *args, **options):

        # Удаление данных таблиц
        Category.objects.all().delete()
        Product.objects.all().delete()

        # Формирование списка полей для таблицы "Категории"
        category_list = [
            {'id': 1, 'category_name': 'Телефон', 'category_description': 'Используется чтобы звонить'},
            {'id': 2, 'category_name': 'Смартфон', 'category_description': 'Чтобы звонить, но может и в интернет'},
            {'id': 3, 'category_name': 'Планшет', 'category_description': 'Для всего, чего угодно, кроме "Звонить"'},
        ]

        # Формирование списка объектов класса Category для распаковки
        category_for_create = []
        for category_item in category_list:
            category_for_create.append(
                Category(**category_item)
            )

        # Запись данных в таблицу сategory
        Category.objects.bulk_create(category_for_create)

        # Формирование списка полей для таблицы "Продукты"
        product_list = [
            {'id': 1, 'product_name': 'Samsung SM-B310', 'product_description': 'Звонилка', 'image_preview': '',
             'category': Category.objects.get(pk=1), 'price': 1100, 'creation_date': "2023-08-11T20:58:01Z",
             'change_date': "2023-08-12T20:58:01Z"},
            {'id': 2, 'product_name': 'LG W41 Plus', 'product_description': 'Не просто звонилка', 'image_preview': '',
             'category': Category.objects.get(pk=2), 'price': 3500, 'creation_date': "2023-09-11T20:58:01Z",
             'change_date': "2023-09-20T10:58:01Z"},
            {'id': 3, 'product_name': 'DEXP Ursus K17', 'product_description': 'Как смартфон, но большой',
             'image_preview': '', 'category': Category.objects.get(pk=3), 'price': 4100,
             'creation_date': "2022-04-11T13:58:01Z", 'change_date': "2022-06-14T10:58:01Z"},
        ]

        # Формирование списка объектов класса Product для распаковки
        product_for_create = []
        for product_item in product_list:
            product_for_create.append(
                Product(**product_item)
            )

        # Запись данных в таблицу product
        Product.objects.bulk_create(product_for_create)
