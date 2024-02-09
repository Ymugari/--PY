import doctest


class Tree:
    """
        Создание и подготовка к работе объекта "Дерево"

        :param size: Размер дерева
        :param family: Семейство дерева

        Примеры:
        >>> tree = Tree(500, "Береза")  # инициализация экземпляра класса
    """
    def __init__(self, size: int, family: str):
        if size <= 0:
            raise ValueError("Дерева с таким размером не существует")
        if not isinstance(size, int):
            raise TypeError("Дерево должно иметь размер типа \'int\'")
        self.size = size
        acceptable_family = ["Дуб", "Береза", "Ель", "Ива", "Клен", "Осина", "Сосна"]
        if family not in acceptable_family:
            raise TypeError(f"Дерево должно принадлежать одному из следующих семейств: {acceptable_family}")
        self.family = family

    def make_planks(self):
        """
            Функция которая делает из дерева доски

            :return: Возвращает количество полученных досок

            Примеры:
            >>> tree = Tree(500, "Береза")
            >>> tree.make_planks()
        """
        ...

    def collect_fruits(self) -> int:
        """
            Функция которая собирает урожай с дерева

            :return: Возвращает количество полученного урожая

            Примеры:
            >>> tree = Tree(500, "Береза")
            >>> tree.collect_fruits()
        """
        ...


class Table:
    """
        Создание и подготовка к работе объекта "Стол"

        :param length: Длина стола
        :param width: Ширина стола

        Примеры:
        >>> table = Table(500, 600)  # инициализация экземпляра класса
    """
    def __init__(self, length: int, width: int):
        if length <= 0 or width <= 0:
            raise ValueError("Стола с такой длинной не существует")
        if not isinstance(length, int) or not isinstance(width, int):
            raise TypeError("Параметры стола должны быть типа: \'int\'")
        self.length = length
        self.widgth = width

    def calculate_square(self, length, width) -> int:
        """
            Функция которая считает площадь стола

            :return: Возвращает площадь стола

            Примеры:
            >>> table = Table(500, 600)
            >>> table.calculate_square(500, 600)
        """
        ...

    def clean_table(self) -> bool:
        """
            Функция которая проверяет чистый ли стол

            :return: Возвращает True или False

            Примеры:
            >>> table = Table(500, 600)
            >>> table.clean_table()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
