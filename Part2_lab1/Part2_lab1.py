import doctest


class Vehicle:
    def __init__(self, brand: str, model: str):
        """
        Создание объекта "Автомобиль".

        :param brand: Марка автомобиля
        :param model: Модель автомобиля

        Примеры:
        >>> car = Vehicle("Toyota", "Camry")  # инициализация экземпляра класса
        """
        self.brand = brand
        self.model = model

    def start_engine(self) -> None:
        """
        Запуск двигателя автомобиля.

        Примеры:
        >>> car = Vehicle("Toyota", "Camry")
        >>> car.start_engine()
        """
        ...

    def stop_engine(self) -> None:
        """
        Остановка двигателя автомобиля.

        Примеры:
        >>> car = Vehicle("Toyota", "Camry")
        >>> car.stop_engine()
        """
        ...


class Book:
    def __init__(self, title: str, author: str, genre: str):
        """
        Создание объекта "Книга".

        :param title: Название книги
        :param author: Автор книги
        :param genre: Жанр книги

        Примеры:
        >>> book = Book("1984", "George Orwell", "Дистопия")  # инициализация экземпляра класса
        """
        self.title = title
        self.author = author
        self.genre = genre

    def open_book(self, page: int) -> str:
        """
        Открытие страницы в книге.

        :param page: Номер страницы для открытия
        :return: Содержание страницы

        Примеры:
        >>> book = Book("1984", "George Orwell", "Дистопия")
        >>> book.open_book(10)
        """
        ...

    def close_book(self) -> None:
        """
        Закрытие книги.

        Примеры:
        >>> book = Book("1984", "George Orwell", "Дистопия")
        >>> book.close_book()
        """
        ...


class MusicTrack:
    def __init__(self, title: str, artist: str, duration: float):
        """
        Создание объекта "Музыкальный трек".

        :param title: Название трека
        :param artist: Исполнитель трека
        :param duration: Продолжительность трека в минутах

        Примеры:
        >>> track = MusicTrack("Shape of You", "Ed Sheeran", 3.54)  # инициализация экземпляра класса
        """
        self.title = title
        self.artist = artist
        self.duration = duration

    def play_track(self) -> None:
        """
        Воспроизведение музыкального трека.

        Примеры:
        >>> track = MusicTrack("Shape of You", "Ed Sheeran", 3.54)
        >>> track.play_track()
        """
        ...

    def pause_track(self) -> None:
        """
        Пауза в воспроизведении музыкального трека.

        Примеры:
        >>> track = MusicTrack("Shape of You", "Ed Sheeran", 3.54)
        >>> track.pause_track()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации