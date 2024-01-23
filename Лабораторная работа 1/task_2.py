# TODO Найдите количество книг, которое можно разместить на дискете
size_of_diskette = 1.44 * 1024 * 1024  # in bytes
count_pages = 100
strings_in_page = 50
chars_in_string = 25
need_for_char = 4
size_of_book = need_for_char * chars_in_string * strings_in_page * count_pages
count_of_books = size_of_diskette // size_of_book
count_of_books = int(count_of_books)
print("Количество книг, помещающихся на дискету:", count_of_books)
