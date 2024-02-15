class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        """Делаем protected атрибуты"""
        self._name = name
        self._author = author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"

    @property
    def name(self) -> str:
        """Возвращает название книги."""
        return self._name

    @property
    def author(self) -> str:
        """Возвращает автора книги."""
        return self._author


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)  # Наследуем атрибуты базового класса
        if not isinstance(self._pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if self._pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self._pages = pages

    def __repr__(self):
        """Перегружаем магический метод __repr__"""
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self._pages})"

    @property
    def pages(self) -> int:
        """Возвращает количество страниц в книге."""
        return self._pages

    @pages.setter
    def pages(self, new_pages: int) -> None:
        """Устанавливает количество страниц в книге."""
        if not isinstance(new_pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if new_pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self._pages = new_pages


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)  # Наследуем атрибуты базового класса
        if not isinstance(self._duration, float):
            raise TypeError("Длительность аудиокниги должна быть типа float")
        if self._duration <= 0:
            raise ValueError("Длительность аудиокниги должна быть положительным числом")
        self._duration = duration

    def __repr__(self):
        """Перегружаем магический метод __repr__"""
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self._duration})"

    @property
    def duration(self) -> float:
        """Возвращает длительность аудиокниги."""
        return self._duration

    @duration.setter
    def duration(self, new_duration: float) -> None:
        """Устанавливает длительность аудиокниги."""
        if not isinstance(new_duration, float):
            raise TypeError("Длительность аудиокниги должна быть типа float")
        if new_duration <= 0:
            raise ValueError("Длительность аудиокниги должна быть положительным числом")
        self._duration = new_duration
