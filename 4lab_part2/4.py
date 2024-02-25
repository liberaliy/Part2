from typing import Union

class Vehicle:
    """
    Базовый класс для транспортных средств.
    """
    def __init__(self, brand: str, model: str, year: int):
        """
        Конструктор базового класса.

        Args:
            brand (str): Марка транспортного средства.
            model (str): Модель транспортного средства.
            year (int): Год выпуска транспортного средства.
        """
        self._brand = brand
        self._model = model
        self._year = year

    def get_description(self) -> str:
        """
        Возвращает описание транспортного средства.

        Returns:
            str: Описание транспортного средства.
        """
        return f"{self._year} {self._brand} {self._model}"

    def move(self, speed: float) -> str:
        """
        Метод для движения транспортного средства.

        Args:
            speed (float): Скорость движения.

        Returns:
            str: Сообщение о движении.
        """
        return f"{self.get_description()} движется со скоростью {speed} км/ч."

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта.

        Returns:
            str: Строковое представление объекта.
        """
        return self.get_description()

    def __repr__(self) -> str:
        """
        Возвращает представление объекта для отладки.

        Returns:
            str: Представление объекта для отладки.
        """
        return f"Vehicle(brand={self._brand}, model={self._model}, year={self._year})"


class Car(Vehicle):
    """
    Дочерний класс для легкового автомобиля.
    """
    def __init__(self, brand: str, model: str, year: int, color: str):
        """
        Конструктор дочернего класса.

        Args:
            brand (str): Марка автомобиля.
            model (str): Модель автомобиля.
            year (int): Год выпуска автомобиля.
            color (str): Цвет автомобиля.
        """
        super().__init__(brand, model, year)
        self._color = color

    def honk(self) -> str:
        """
        Унаследованный метод для звукового сигнала автомобиля.

        Returns:
            str: Звуковой сигнал автомобиля.
        """
        return f"{self.get_description()} издает звуковой сигнал 'Бип-бип!'"

    def __repr__(self) -> str:
        """
        Возвращает представление объекта для отладки.

        Returns:
            str: Представление объекта для отладки, включая цвет.
        """
        return f"Car(brand={self._brand}, model={self._model}, year={self._year}, color={self._color})"
