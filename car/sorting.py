from abc import ABC, abstractmethod


class Sorting(ABC):
    @abstractmethod
    def sort_cars(self, cars, descending):
        pass


class SortingComponents(Sorting):
    def sort_cars(self, cars, descending):
        """
        Sort cars by the number of components
        """
        return sorted(cars, key=lambda item: len(item.car_body.components), reverse=descending)


class SortingEnginePower(Sorting):
    def sort_cars(self, cars, descending):
        """
        Sort cars by engine power
        """
        return sorted(cars, key=lambda item: item.engine.power, reverse=descending)


class SortingWheelSize(Sorting):
    def sort_cars(self, cars, descending):
        """
        Sort cars by wheel size
        """
        return sorted(cars, key=lambda item: item.wheel.size, reverse=descending)
