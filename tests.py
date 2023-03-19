from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_add_new_book_add_two_same_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две одинаковые книги
        collector.add_new_book('Война и мир')
        collector.add_new_book('Война и мир')

        # проверяем, что добавилась именно одна
        assert len(collector.get_books_rating()) == 1


    def test_set_book_rating_not_listed_book(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        #устанавливаем рейтинг несуществующей книге
        collector.set_book_rating('Вино из одуванчиков',8)
        #проверяем, что книге не установлен рейтинг
        assert collector.get_book_rating('Вино из одуванчиков') is None

    def test_set_book_rating_below_one(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем книгу
        collector.add_new_book('Убийство в Восточном экспрессе')
        # устанавливаем книге рейтинг, меньше 1
        collector.set_book_rating('Убийство в Восточном экспрессе', -1)
        # проверяем, что рейтинг остался равным 1
        assert collector.get_book_rating('Убийство в Восточном экспрессе') == 1

    def test_set_book_rating_above_ten(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        # добавляем книгу
        collector.add_new_book('Анна Каренина')
        # устанавливаем книге рейтинг, больше 10
        collector.set_book_rating('Анна Каренина', 11)
        # проверяем, что рейтинг остался равным 1
        assert collector.get_book_rating('Анна Каренина') == 1

    def test_set_book_rating_string_value(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        # добавляем книгу
        collector.add_new_book('Анна Каренина')
        # устанавливаем книге рейтинг 'test'
        collector.set_book_rating('Анна Каренина', 'test')
        # проверяем, что рейтинг остался равным 1
        assert collector.get_book_rating('Анна Каренина') == 1

    def test_get_book_rating_not_listed_book(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        #проверяем, что у несуществующей книги нет рейтинга
        assert collector.get_book_rating('451 градус по Фаренгейту') is None

    def test_add_book_in_favorites_add_two_books_in_favorite(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        # добавляем книги  в коллекцию
        collector.add_new_book('Бесы')
        collector.add_new_book('Братья Карамазовы')
        # добавляем книги в "Избранное"
        collector.add_book_in_favorites('Бесы')
        collector.add_book_in_favorites('Братья Карамазовы')
        # проверяем, что добавленные книги в "Избранном"
        assert 'Бесы' in collector.get_list_of_favorites_books() and 'Братья Карамазовы' in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_not_listed_book(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        collector.add_book_in_favorites('Оливер Твист')
        assert 'Оливер Твист' not in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_delete_book(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        collector.add_new_book('Братья Карамазовы')
        collector.add_book_in_favorites('Братья Карамазовы')
        collector.delete_book_from_favorites('Братья Карамазовы')
        assert 'Братья Карамазовы' not in collector.get_list_of_favorites_books()

    def test_default_value_books_rating_of_collector_true(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        # проверяем корректную инициализацию свойства books_rating
        assert collector.books_rating == {}

    def test_default_value_favorites_of_collector_true(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        # проверяем корректную инициализацию свойства favorites
        assert collector.favorites == []

    def test_get_books_with_specific_rating_show(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        collector.add_new_book('Кот в сапогах')
        collector.set_book_rating('Кот в сапогах', 10)

        collector.add_new_book('Война и мир')
        collector.set_book_rating('Война и мир', 9)

        assert 'Кот в сапогах' in collector.get_books_with_specific_rating(10)
