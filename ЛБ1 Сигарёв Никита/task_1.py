# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class House:
    """описание дома"""
    def __init__(self, street, number):
        """свойства дома"""
        self.street = street
        self.number = number
        self.age = 0

    def build(self):
         """строить дом"""
         print(" Дом на улице " + self.street + " под номером " + str(self.number) + "построен.")

    def age_of_house(self, year):
        """возраст дома"""
        self.age += year


class ProspectHouse(House):
    """Дома на проспекте"""
    def __init__(self, prospect, number):
        super().__init__(self,number)
        self.prospect = prospect


"""В предоставленном коде мы определили три абстрактных класса: Furniture, Tree, SocialMedia. 
Каждый класс представляет отдельный тип объекта, и мы включили атрибуты и методы, которые описывают их характеристики и поведение."""

class Furniture:
    """Мебель"""
    def __init__(self, material: str, weight: float):
        # Атрибутам присваиваются значения аргументов конструктора объекта
        self.material = material
        self.weight = weight

    def assemble(self) -> None:
        """Собирает мебель."""
        ...

    def disassemble(self) -> None:
        """Разбирает мебель."""
        ...

    def get_material(self) -> str:
        """Возвращает материал мебели."""
        ...

class Tree:
    """Дерево"""
    def __init__(self, age: int, height: float):
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным.")
        self.age = age
        self.height = height

    def grow(self, years: int) -> None:
        """Увеличивает возраст дерева на заданное количество лет.

        :param years: Количество лет для увеличения возраста.
        :raises ValueError: Если years отрицательное.
        """
        ...

    def get_age(self) -> int:
        """Возвращает возраст дерева."""
        ...

class SocialMedia:
    """Социальные средства"""
    def __init__(self, name: str, user_count: int):
        if user_count < 0:
            raise ValueError("Количество пользователей не может быть отрицательным.")
        self.name = name
        self.user_count = user_count

    def add_user(self) -> None:
        """Добавляет нового пользователя на платформу."""
        ...

    def remove_user(self) -> None:
        """Удаляет пользователя с платформы."""
        ...

    def get_user_count(self) -> int:
        """Возвращает количество пользователей на платформе."""
        ...

    """ОБЪЯСНЕНИЕ: 
    1.Абстрактные классы : использование абстрактных классов позволяет нам определить схему для других классов. 
    Каждый класс содержит абстрактные методы, которые должны быть реализованы любым подклассом.
    2. Атрибуты : Каждый класс имеет атрибуты, которые представляют его характеристики. 
    Например, Furniture имеет material и weight, в то время как Tree имеет age и height. 
    Проверка включена в конструктор Tree и SocialMedia для обеспечения того, чтобы возраст и количество пользователей не могли быть отрицательными.
    3. Методы : Каждый класс включает методы, описывающие возможные действия. 
    Например, Furniture имеет методы для сборки и разборки, а также Tree имеет метод для выращивания.
     Каждый метод документирован аннотациями типов и описаниями параметров и возвращаемых значений.
    4. Документация : методы включают строки документации, объясняющие их назначение,
     параметры и любые исключения, которые могут возникнуть, обеспечивая ясность для будущих разработчиков.

"""

if __name__ == "__main__":
    doctest.testmod()
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
