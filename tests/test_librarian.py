import unittest
import librarian as lb

class TestLibrarian(unittest.TestCase):

    def setUp(self):

        self.books = [
            {'number': 'P-1234', 'title': 'Евгений Онегин', 'author': 'Александр Пушкин'},
            {'number': 'F-88006', 'title': 'Властелин колец', 'author': 'Джон Р. Р. Толкин'},
            {'number': 'D-1122', 'title': 'Безмолвный свидетель', 'author': 'Агата Кристи'}
        ]

        self.directories = {
            '1': ['P-1234', 'F-88006'],
            '2': ['D-1122'],
            '3': []
        }

    def test_get_book(self):
        self.assertEqual(lb.get_book(self.books, 'P-1234'),
                         'Книга: Евгений Онегин\nАвтор: Александр Пушкин')
        self.assertEqual(lb.get_book(self.books, 'P-1235'), 'Книга не найдена в базе')

    def test_get_shelf(self):
        self.assertEqual(lb.get_shelf(self.directories, 'D-1122'), '2')
        self.assertEqual(lb.get_shelf(self.directories, 'A-1122'),
                         'Полки с такой книгой не найдено')

    def test_add_book(self):
        self.assertEqual(lb.add_book(self.books, self.directories, 'P-1234','Евгений Онегин',
                                     'Александр Пушкин', '3'), 'Такая книга уже есть в списке')
        self.assertEqual(lb.add_book(self.books, self.directories, 'N-5678','Война и мир',
                                     'Лев Толстой', '3'), 'Книга добавлена на полку: 3')