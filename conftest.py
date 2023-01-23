import pytest
from main import BooksCollector

@pytest.fixture  # фикстура, которая создаёт коллекцию с 4 книгами, одна с рейтингом 7, одна в favorites
def my_collection():
    my_collection = BooksCollector()
    my_collection.add_new_book('Тихий дон')
    my_collection.add_new_book('Молодая гвардия')
    my_collection.add_new_book('Судьба человека')
    my_collection.add_new_book('Они сражались за родину')
    my_collection.set_book_rating('Они сражались за родину', 7)
    my_collection.add_book_in_favorites('Молодая гвардия')

    return my_collection