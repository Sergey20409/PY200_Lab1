from typing import Union
import doctest

class Tanker:
    def __init__(self, capacity_volume: Union[int, float], crew: int, occupied_volume: Union[int, float]):

        self.capacity_volume = capacity_volume
        self.crew = crew
        self.occupied_volume = occupied_volume

        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("Тип должен быть или int или float")
        if not capacity_volume > 0:
            raise ValueError("Объем танкера должен быть больше 0")

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError("Тип должен быть или int или float")
        if not occupied_volume > 0:
            raise ValueError("Не должно быть отрицательных значений")
        if occupied_volume > capacity_volume:
            raise ValueError("Наполнить танкер больше того, что возможно нельзя")

        if not isinstance(crew, int):
            raise TypeError("Тип должен быть или int")
        if crew < 0:
            raise ValueError("Экипаж должен быть больше 0")
        if crew > 30:
            raise ValueError("Экипаж не может быть больше 30")

    def add_crew_on_tanker(self, add_crew: int) -> None:
        """
        Добавление членов экипажа на танкер.

        :param add_crew: Количество добавляемых членов экипажа

        :raise ValueError: Если количество добавляемых людей превышает количество мест, то вызываем ошибку

        :raise ValueError: Если количество добавляем людей отрицательное значение, то вызываем ошибку

        :raise TypeError: Количество людей должно быть целым числом

        >>> tanker1 = Tanker(20, 25, 10)
        >>> tanker1.add_crew_on_tanker(7)
        Traceback (most recent call last):
        ValueError: Экипаж не может быть больше 30
        >>> tanker1.add_crew_on_tanker(0.5)
        Traceback (most recent call last):
        TypeError: Количество людей должно быть целым числом
        >>> tanker1.add_crew_on_tanker(-5)
        Traceback (most recent call last):
        ValueError: Количество людей должно быть положительным значением
        """

        if not isinstance(add_crew, int):
            raise TypeError("Количество людей должно быть целым числом")
        if add_crew < 0:
            raise ValueError("Количество людей должно быть положительным значением")
        if self.crew + add_crew > 30:
            raise ValueError("Экипаж не может быть больше 30")
        self.crew += add_crew


class Bulker:
    def __init__(self, capacity_weight: Union[int, float], crane:int, occupied_weight: Union[int, float]):

        self.capacity_weight = capacity_weight
        self.crane = crane
        self.occupied_weight = occupied_weight

        if not isinstance(capacity_weight, (int, float)):
            raise TypeError("Тип должен быть или int или float")
        if not capacity_weight > 0:
            raise ValueError("Масса груза должна быть больше 0")

        if not isinstance(occupied_weight, (int, float)):
            raise TypeError("Тип должен быть или int или float")
        if not occupied_weight > 0:
            raise ValueError("Не должно быть отрицательных значений")
        if occupied_weight > capacity_weight:
            raise ValueError("Наполнить танкер больше того, что возможно нельзя")

        if not isinstance(crane, int):
            raise TypeError("Тип должен быть int")

        if not crane > 0:
            raise ValueError("Кранов должен быть больше 0")
        if crane > 5:
            raise ValueError("Кранов не может быть больше 5")



class Supply_Tug:
    def __init__(self, hook_force: Union[int, float], capacity_container:int, occupied_container:int):

        self.hook_force = hook_force
        self.capacity_container = capacity_container
        self.occupied_container = occupied_container

        if not isinstance(hook_force, (int, float)):
            raise TypeError("Тип должен быть или int или float")
        if hook_force < 0:
            raise ValueError("Усилие буксира должно быть больше 0")

        if not isinstance(capacity_container, (int)):
            raise TypeError("Тип должен быть int")
        if capacity_container < 0:
            raise ValueError("Количество контейнеров должно быть больше 0")


        if not isinstance(occupied_container, (int)):
            raise TypeError("Тип должен быть int")
        if occupied_container < 0:
            raise ValueError("Не должно быть отрицательных значений")
        if occupied_container > capacity_container:
            raise ValueError("Взять контейнеров больше чем мест, нельзя")


    def add_cont_on_tug(self, add_cont: int) -> None:
        """
        Добавление контейнеров на буксир.

        :param add_cont: Количество добавляемых контейнеров

        :raise ValueError: Если количество добавляемых контейнеров превышает количество мест, то вызываем ошибку

        :raise ValueError: Если количество контенеров отрицательное значение, то вызываем ошибку

        :raise TypeError: Количество контейнеров должно быть целым числом

        >>> tug2 = Supply_Tug(20, 25, 10)
        >>> tug2.add_cont_on_tug(30)
        Traceback (most recent call last):
        ValueError: Количество контейнеров не может быть больше вместимости
        >>> tug2.add_cont_on_tug(0.5)
        Traceback (most recent call last):
        TypeError: Количество контейнеров должно быть целым числом
        >>> tug2.add_cont_on_tug(-5)
        Traceback (most recent call last):
        ValueError: Количество контейнеров должно быть положительным значением
        """

        if not isinstance(add_cont, int):
            raise TypeError("Количество контейнеров должно быть целым числом")
        if add_cont < 0:
            raise ValueError("Количество контейнеров должно быть положительным значением")
        if self.occupied_container + add_cont  > self.capacity_container:
            raise ValueError("Количество контейнеров не может быть больше вместимости")
        self.occupied_container += add_cont


if __name__ == "__main__":
    tanker1 = Tanker(20, 25, 10)  # экземпляр класса
    print("Водоизмещение танкера - ", tanker1.capacity_volume, "; Команда танкера - ", tanker1.crew, "; Занятый объем танков - ", tanker1.occupied_volume,';')

    bulker1 = Bulker(10, 3, 5)  # экземпляр класса
    print("Водоизмещение сухогруза - ",bulker1.capacity_weight, "; Количество кранов - ", bulker1.crane, "; Количество груза в трюмах - ", bulker1.occupied_weight,';')

    tug1 = Supply_Tug(50,20,19)# экземпляр класса
    print("Тяговое усилие буксира -", tug1.hook_force, "; Контейнеровместимость - ", tug1.capacity_container, "; Контейнеров на борту - ", tug1.occupied_container,';')

if __name__ == "__main__":
    doctest.testmod()