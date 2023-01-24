import pytest
from main import BooksCollector


# проверка существования 1 метода "конструктора" __init__, также метода get_books_rating
def test_books_rating_dict_exist(my_collection):
    assert my_collection.books_rating == {'Молодая гвардия': 1,
                                          'Судьба человека': 1,
                                          'Тихий дон': 1,
                                          'Они сражались за родину': 7}


# проверка существования 2 метода "конструктора" __init__, а также метода get_list_of_favorites_books
def test_favorites_list_exist(my_collection):
    assert my_collection.favorites == ['Молодая гвардия']


# проверка добвления книги - изменение словаря
def test_add_new_book_new_book_books_rating_exist(my_collection):
    my_collection.add_new_book('Поднятая целина')

    assert my_collection.books_rating == {'Молодая гвардия': 1,
                                          'Они сражались за родину': 7,
                                          'Поднятая целина': 1,
                                          'Судьба человека': 1,
                                          'Тихий дон': 1}


# проверка изменения рейтинга в диапазоне
def test_set_book_rating_new_rate_books_rating_change(my_collection):
    my_collection.set_book_rating('Тихий дон', 6)

    assert my_collection.books_rating['Тихий дон'] == 6


# проерка изменения рейтинга вне диапазона - рейтинг остается прежним
def test_set_book_rating_rate_out_of_range_books_rating_no_change(my_collection):
    my_collection.set_book_rating('Тихий дон', 22)

    assert my_collection.books_rating['Тихий дон'] == 1


# проверка изменения рейтинга у книги
def test_get_book_rating_dic_name_value(my_collection):
    my_collection.set_book_rating('Судьба человека', 7)

    assert my_collection.books_rating['Судьба человека'] == 7


# проверка списка книг по рейтингу
def test_get_books_with_specific_rating_rate_list_exists(my_collection):
    my_collection.set_book_rating('Судьба человека', 7)

    assert my_collection.get_books_with_specific_rating(7) == ['Судьба человека', 'Они сражались за родину']


class TestFav:
    @pytest.mark.usefixtures('simple_collection')
# проверка добавления книги в список favorites
    def test_add_book_in_favorites_new_book_list_increase(self, simple_collection):
        simple_collection.add_book_in_favorites('Тихий дон')

        assert simple_collection.favorites == ['Молодая гвардия', 'Тихий дон']

# проверка удаления книги из списка favorites
    def test_delete_book_from_favorites_book_list_decrease(self, simple_collection):
        simple_collection.delete_book_from_favorites('Молодая гвардия')

        assert simple_collection.favorites == []

# проверка параметризованого теста
@pytest.mark.parametrize("name,rate", [('Судьба человека', 7), ('Молодая гвардия', 8), ('Поднятая целина', 9)])
def test_set_books_with_specific_rating_rate_list_correct(name, rate):

    rating_collection = BooksCollector()
    rating_collection.add_new_book(name)
    rating_collection.set_book_rating(name, rate)

    assert rating_collection.books_rating[name] == rate