import pytest

class TestBooksCollector:

    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.books_genre) == 2

    @pytest.mark.parametrize('name', [
        'Гордость и предубеждение',
        'Tom Sawyer',
        'Мастер и Маргарита'
    ])
    def test_add_new_book_success(self, collector, name):
        collector.add_new_book(name)
        assert name in collector.books_genre

    def test_add_new_book_two_books_with_same_name(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')

        assert len(collector.books_genre) == 1

    def test_add_new_book_book_with_too_long_name(self, collector):
        collector.add_new_book('Это название книги которое больше 41 букв')

        assert len(collector.books_genre) == 0

    def test_set_book_genre_add_book_with_genre(self, collector):
        collector.add_new_book('Преступление и наказание')
        collector.set_book_genre('Преступление и наказание', 'Ужасы')

        assert collector.books_genre['Преступление и наказание'] == 'Ужасы'

    def test_set_book_genre_add_book_with_genre_not_in_list(self, collector):
        collector.add_new_book('Мастер и Маргарита')
        collector.set_book_genre('Мастер и Маргарита', 'Роман')

        assert collector.books_genre['Мастер и Маргарита'] == ''

    def test_get_book_genre_success(self, collector):
        collector.add_new_book('Преступление и наказание')
        collector.set_book_genre('Преступление и наказание', 'Ужасы')

        assert collector.get_book_genre('Преступление и наказание') == 'Ужасы'


    def test_get_books_with_specific_genre(self, collector):
        collector.books_genre = {
            'Служебный роман': '',
            'Ну погоди!': '',
            'Кавказская пленница': ''
        }
        collector.set_book_genre('Служебный роман', 'Комедии')
        collector.set_book_genre('Ну погоди!', 'Мультфильмы')
        collector.set_book_genre('Кавказская пленница', 'Комедии')

        assert len(collector.get_books_with_specific_genre('Комедии')) == 2

    def test_get_books_with_specific_genre_genre_not_in_list(self, collector):
        collector.books_genre = {
            'Служебный роман': 'Комедии',
            'Ну погоди!': 'Мультфильмы',
            'Кавказская пленница': 'Фэнтези'
        }

        assert collector.get_books_with_specific_genre('Фэнтези') == []

    def test_get_books_genre_success(self, collector):
        collector.books_genre = {
            'Служебный роман': 'Комедии'}
        assert collector.get_books_genre() == {'Служебный роман': 'Комедии'}

    def test_get_books_for_children_not_return_book_with_age_rating(self, collector):
        collector.books_genre = {
            'Служебный роман': 'Комедии',
            'Пила': 'Ужасы'
        }

        assert len(collector.get_books_for_children()) == 1

    def test_add_book_in_favorites_success(self, collector):
        collector.books_genre = {
            'Служебный роман': 'Комедии'
        }
        collector.add_book_in_favorites('Служебный роман')

        assert 'Служебный роман' in collector.favorites

    def test_add_book_in_favorites_not_add_duplicate(self, collector):
        collector.books_genre = {
            'Служебный роман': 'Комедии'
        }
        collector.favorites = ['Служебный роман']
        collector.add_book_in_favorites('Служебный роман')

        assert len(collector.favorites) == 1

    def test_delete_book_from_favorites_success(self, collector):
        collector.favorites = ['Служебный роман', 'Терминатор']
        collector.delete_book_from_favorites('Терминатор')

        assert 'Терминатор' not in collector.favorites

    def test_get_list_of_favorites_books_success(self, collector):
        collector.favorites = ['Служебный роман', 'Терминатор']

        assert len(collector.get_list_of_favorites_books()) == 2












