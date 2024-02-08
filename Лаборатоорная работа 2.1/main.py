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


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
