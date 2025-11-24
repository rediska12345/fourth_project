from main import BooksCollector

@pytest.fixture
def collector():
    return BooksCollector()   

class TestBooksCollector:
    
    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_rating()) == 2

    @pytest.mark.parametrize("book_name", ["Книга1","A" * 40]) # Добавления книг с валидной длиной названия
    
    def test_add_new_book_valid_names(self, collector, book_name):
        collector.add_new_book(book_name)
        assert book_name in collector.get_books_genre()

    @pytest.mark.parametrize("book_name", ["","A" * 41]) #тест для названий книг с недопустимой длиной

    def test_add_new_book_invalid_names(self, collector, book_name):
        collector.add_new_book(book_name)
        assert book_name not in collector.get_books_genre()

    def test_add_new_book_duplicate(self, collector):
        collector.add_new_book('Книга1')
        collector.add_new_book('Книга1')
        assert len(collector.get_books_genre()) == 1 # Тест добавления одной и той же книги дважды

    def test_set_and_get_book_genre(self, collector):
        collector.add_new_book('Книга1')
        collector.set_book_genre('Книга1', 'Фантастика')
        assert collector.get_book_genre('Книга1') == 'Фантастика' # Тест установки и получения жанра книги

    def test_set_book_genre_invalid(self, collector):
        collector.add_new_book('Книга1')
        collector.set_book_genre('Книга1', 'Неизвестный жанр')
        assert collector.get_book_genre('Книга1') == '' # Тест попытки установить недопустимый жанр

    def test_get_books_with_specific_genre(self, collector):
        collector.add_new_book('Книга1')
        collector.add_new_book('Книга2')
        collector.set_book_genre('Книга1', 'Фантастика')
        collector.set_book_genre('Книга2', 'Ужасы')
        books = collector.get_books_with_specific_genre('Фантастика')
        assert 'Книга1' in books and 'Книга2' not in books # Тест получения списка книг с определённым жанром

    def test_get_books_genre(self, collector):
        collector.add_new_book('Книга1')
        collector.add_new_book('Книга2')
        collector.set_book_genre('Книга1', 'Фантастика')
        collector.set_book_genre('Книга2', 'Ужасы')
        genres = collector.get_books_genre()
        expected = {'Книга1':'Фантастика','Книга2': 'Ужасы'}
        assert genres == expected

    def test_get_books_for_children(self, collector):
        collector.add_new_book('Книга1')
        collector.add_new_book('Книга2')
        collector.set_book_genre('Книга1', 'Комедии')  
        collector.set_book_genre('Книга2', 'Ужасы')    
        children_books = collector.get_books_for_children()
        assert 'Книга1' in children_books and 'Книга2' not in children_books # Тест получения книг, подходящих для детей

    def test_add_and_get_favorites(self, collector):
        collector.add_new_book('Книга1')
        collector.add_book_in_favorites('Книга1')
        favs = collector.get_list_of_favorites_books()
        assert 'Книга1' in favs  # Тест добавления книги в избранное и получение списка избранных

    def test_add_favorite_book_multiple_times(self, collector):
        collector.add_new_book('Книга1')
        collector.add_book_in_favorites('Книга1')
        collector.add_book_in_favorites('Книга1')
        assert len(collector.get_list_of_favorites_books()) == 1 # Тест, что одну и ту же книгу нельзя добавить в избранное дважды

    def test_delete_book_from_favorites(self, collector):
        collector.add_new_book('Книга1')
        collector.add_book_in_favorites('Книга1')
        collector.delete_book_from_favorites('Книга1')
        assert 'Книга1' not in collector.get_list_of_favorites_books()  # Тест удаления книги из избранного

