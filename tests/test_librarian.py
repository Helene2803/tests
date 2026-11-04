import pytest
import librarian as lb

params = (
    ([{'number': 'P-1234', 'title': 'Евгений Онегин', 'author': 'Александр Пушкин'}],
     'P-1234',
     'Книга: Евгений Онегин\nАвтор: Александр Пушкин'),
    ([{'number': 'P-1234', 'title': 'Евгений Онегин', 'author': 'Александр Пушкин'}],
    'P-1235',
    'Книга не найдена в базе')
)

@pytest.mark.parametrize(
    'books, book_number, expected',
    params
)
def test_get_book(books, book_number, expected):
    assert lb.get_book(books, book_number) == expected

params = (
    ({'1': ['P-1234', 'F-88006'], '2': ['D-1122'], '3': []},
    'D-1122',
     '2'),
    ({'1': ['P-1234', 'F-88006'], '2': ['D-1122'], '3': []},
     '12345',
     'Полки с такой книгой не найдено')
)

@pytest.mark.parametrize(
    'directories, book_number, expected',
    params
)

def test_get_shelf(directories, book_number, expected):
    assert lb.get_shelf(directories, book_number) == expected

params = (
    ([{'number': 'D-1122', 'title': 'Безмолвный свидетель', 'author': 'Агата Кристи'}],
     {'1': ['P-1234', 'F-88006'], '2': ['D-1122'], '3': []},
     'N-5678',
     'Война и мир',
     'Лев Толстой',
     '3',
     'Книга добавлена на полку: 3',
     [{'number': 'D-1122', 'title': 'Безмолвный свидетель', 'author': 'Агата Кристи'},
      {'number': 'N-5678', 'title': 'Война и мир', 'author': 'Лев Толстой'}],
     {'1': ['P-1234', 'F-88006'], '2': ['D-1122'], '3': ['N-5678']}),
    ([{'number': 'D-1122', 'title': 'Безмолвный свидетель', 'author': 'Агата Кристи'}],
     {'1': ['P-1234', 'F-88006'], '2': ['D-1122'], '3': []},
     'D-1122',
     'Безмолвный свидетель',
     'Агата Кристи',
     '3',
     'Такая книга уже есть в списке',
     [{'number': 'D-1122', 'title': 'Безмолвный свидетель', 'author': 'Агата Кристи'}],
     {'1': ['P-1234', 'F-88006'], '2': ['D-1122'], '3': []})
     )

@pytest.mark.parametrize(
    'books, directories, book_number, title, author, shelf, expected, changed_books, changed_dir',
    params
)

def test_add_book(books, directories, book_number, title, author, shelf, expected, changed_books, changed_dir):
    assert lb.add_book(books, directories, book_number, title, author, shelf) == expected
    assert books == changed_books
    assert directories == changed_dir

