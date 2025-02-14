class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(author={self._author!r})"

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)

        self.pages = pages

    @property
    def pages(self):
        return self._pages
    @pages.setter
    def pages(self, value: int):
        if not isinstance(value, (int)):
            raise TypeError("Количество страниц должно быть целым числом")
        if not value > 0:
            raise ValueError("Количество страниц должно быть положительным числом 0")
        self._pages = value

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.pages!r})'

class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)

        self.duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value: float):
        if not isinstance(value, (float)):
            raise TypeError("Продолжительность должна быть числом с плавающей точкой")
        if not value > 0:
            raise ValueError("Продолжительность должна быть положительным числом 0")
        self._duration = value

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self._name!r}, {self.duration!r})'

if __name__ == "__main__":
    book1 = PaperBook("Идиот", "Достоевский", -700)  # экземпляр класса
    print("Название - ", book1._name, "; Автор - ", book1._author, "; Страницы - ", book1.pages)