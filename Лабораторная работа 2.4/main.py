import random


class Car:
    """Создаем базовый класс автомобили"""

    def __init__(self, name: str, license_plate: str):
        """Создаем конструктор, который будет принимать три атрибута: марка автомобиля, номерной знак
        и состояние машины. Делаем необходимые проверки. Номерной знак мы делаем protected атрибутом,
        так как предполагается, не изменять эти данные."""
        if not isinstance(name, str):
            raise TypeError("Марка автомобиля должна быть типа str")
        self._name = name
        if not isinstance(license_plate, str):
            raise TypeError("Номерной знак должен быть типа str")
        self._license_plate = license_plate  # инициализируем защищенный атрибут
        self.status = 'new'  # Изначально состояние 'новое'

    @property
    def name(self) -> str:
        """Возвращает марку автомобиля."""
        return self._name  # внутри класса обращаемся к защищенному атрибуту

    @property
    def license(self) -> str:
        """Возвращает номерной знак автомобиля."""
        return self._license_plate  # внутри класса обращаемся к защищенному атрибуту

    def __str__(self):
        """Реализуем магический метод __str__"""
        return f'{self.__class__.__name__}: {self.name!r}'

    def __repr__(self):
        """Реализуем магический метод __repr__"""
        return f'{self.__class__.__name__}: {self.name!r}, license plate: {self._license_plate!r}'

    def painting(self, color: str) -> str:
        """Метод делает покраску автомобиля, делаем необходимые проверки и возвращаем строку с тем цветом,
        в который перекрасили машину"""
        if not isinstance(color, str):
            raise TypeError("Выбираемый цвет должен быть str типа")
        colors = ["blue", "red", "green", "black", "white", "yellow", "orange", "gray", "purple"]
        if color not in colors:
            raise TypeError(f'Выбирете один из представленных цветов: {colors}')
        return f'Now your {self.__class__.name} {self._name!r} {color}'

    def car_status(self) -> str:
        """Метод, который будет возвращать новое состояние машины."""
        statuses = ['new', 'minor damage', 'damaged', 'broken']  # Все доступные состояния машины
        current_status = random.choice(statuses)
        self.status = current_status
        return self.status  # Вернет одно из состояний


class PassengerCar(Car):
    """Создаем дочерний класс легковой автомобиль, который унаследован от класса автомобиль. Количество мест
    мы делаем protected атрибутом, так как предполагается, не взаимодействовать с ним,
    но дать пользователю возможность изменять эти данные через метод."""
    def __init__(self, _name: str, _license_plate: str, seats_amount: int):
        """Наследуем конструктор класса автомобиль и добавляем новый атрибут количетсво мест"""
        super().__init__(_name, _license_plate)
        if not isinstance(seats_amount, int):
            raise TypeError("Количество мест должно быть типа int")
        self._seats_amount = seats_amount

    @property
    def seats(self) -> int:
        """Возвращает количество мест в автомобиле."""
        return self._seats_amount

    @seats.setter
    def seats(self, new_amount: int) -> None:
        """Устанавливает количество мест в автомобиле."""
        if not isinstance(new_amount, int):
            raise TypeError("Количество мест должно быть типа int")
        self._seats_amount = new_amount

    def __repr__(self):
        """Перегружаем магический метод __repr__"""
        return (f'{self.__class__.__name__}: {self.name!r}, license plate: {self._license_plate!r}, seats_amount: '
                f'{self._seats_amount}')

    def car_status(self) -> str:
        """Перегружаем метод car_new_status, чтобы он выдавал причину поломки."""
        statuses = ['new', 'minor damage', 'damaged', 'broken']  # Все доступные состояния машины
        current_status = random.choice(statuses)
        self.status = current_status
        reason = ['external damage', 'engine damage', 'cooling system damage', 'locking system']  # Виды проблем машины
        if self.status != 'new':
            current_reason = random.choice(reason)
        else:
            current_reason = 'No problems found'
        return f'Condition of your car {self.status}. Problem: {current_reason}'  # Вернет одно из состояний
