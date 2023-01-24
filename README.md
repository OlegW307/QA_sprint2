## QA_sprint2

## Список реализованных тестов

1. **test_books_rating_dict_exist** - проверка существования 1 метода "конструктора" __init__, также метода get_books_rating

    
2. **def test_favorites_list_exist** - проверка существования 2 метода "конструктора" __init__, а также метода get_list_of_favorites_books
t
   
 
3. **test_add_new_book_new_book_books_rating_exist** - проверка добвления книги - изменение словаря


4. **test_set_book_rating_new_rate_books_rating_change** - проверка изменения рейтинга книги в допустимом диапазоне


5. **test_set_book_rating_rate_out_of_range_books_rating_no_change** - проерка изменения рейтинга вне диапазона - рейтинг остается прежним


6. **test_get_book_rating_dic_name_value** - проверка изменения рейтинга у книги

    
7. **test_get_books_with_specific_rating_rate_list_exists** - проверка списка книг по рейтингу


Обьединение в класс (используется новая фикстура)
9. **test_add_book_in_favorites_new_book_list_increase** - проверка добавления книги в список favorites


10. **test_delete_book_from_favorites_book_list_decrease** - проверка удаления книги из списка favorites

Проверка параметризованного теста (опционально)

11. **test_set_books_with_specific_rating_rate_list_correct** - проверка добавления в список рейтинга с различными значениями


12. **test_new_books_add_with_rating_1** - проверка что новые книги добавляются с рейтингом 1