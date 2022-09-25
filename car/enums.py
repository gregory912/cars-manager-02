from enum import Enum


class SortType(Enum):
    COMPONENTS = 1
    ENGINE_POWER = 2
    WHEEL_SIZE = 3


class Statistic(Enum):
    PRICE = 1
    MILEAGE = 2
    POWER = 3
