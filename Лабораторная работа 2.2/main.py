import doctest


class Book:
    def __init__(self, id_: int, name: str, pages: int):
        """
            Создание и подготовка к работе объекта "Книга"

            :param id_: id_ книги
            :param name: Имя автора
            :param pages: Кол-во страниц

            Примеры:
            >>> book = Book(1, "Пушкин А. С.", 300)  # инициализация экземпляра класса
        """
        self.id_ = id_
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        return f'Книга {self.name}'

    def __repr__(self) -> str:
        return f'Book(id_={self.id_!r}, name={self.name!r}, pages={self.pages!r})'


class Library:
    def __init__(self, books=None):
        """
            Создание и подготовка к работе объекта "Библиотека"

            :param books: книги хранящиеся в библиотеке

            Примеры:
            >>> library = Library()  # инициализация экземпляра класса
        """
        if books is None:
            books = []
        self.books = books

    def get_next_book_id(self) -> int:
        """
            Функция которая возвращает id следующей книгиm, которую мы поместим в библиотеку

            :return: id следующей книги

            Примеры:
            >>> library = Library()
            >>> library.get_next_book_id()
        """
        if not self.books:
            return 1
        else:
            return self.books[-1].id_ + 1

    def get_index_by_book_id(self, id_: int) -> int:
        """
            Функция которая возвращает индекс по id книги

            :return: индекс книги

            Примеры:
            >>> library = Library(books=[Book(1, "Пушкин А. С.", 300)])
            >>> library.get_index_by_book_id(1)
        """
        need_index = None
        for index, value in enumerate(self.books):
            if value.id_ == id_:
                need_index = index
        if need_index is None:
            raise ValueError("Книги с запрашиваемым id не существует")
        else:
            return need_index


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
