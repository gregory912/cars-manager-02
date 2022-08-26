from enum import Enum


class EngineType(Enum):
    DIESEL = 1
    GASOLINE = 2
    LPG = 3

    @classmethod
    def value_of(cls, value: 'EngineType') -> 'EngineType':
        """
        Return an enum object for the entered string
        """
        for k, v in cls.__members__.items():
            if k == value:
                return v
        else:
            raise ValueError(f"'{cls.__name__}' enum not found for '{value}'")


class TyreType(Enum):
    WINTER = 1
    SUMMER = 2

    @classmethod
    def value_of(cls, value: 'TyreType') -> 'TyreType':
        """
        Return an enum object for the entered string
        """
        for k, v in cls.__members__.items():
            if k == value:
                return v
        else:
            raise ValueError(f"'{cls.__name__}' enum not found for '{value}'")


class CarBodyColor(Enum):
    BLACK = 1
    SILVER = 2
    WHITE = 3
    RED = 4
    BLUE = 5
    GREEN = 6

    @classmethod
    def value_of(cls, value: 'CarBodyColor') -> 'CarBodyColor':
        """
        Return an enum object for the entered string
        """
        for k, v in cls.__members__.items():
            if k == value:
                return v
        else:
            raise ValueError(f"'{cls.__name__}' enum not found for '{value}'")


class CarBodyType(Enum):
    SEDAN = 1
    HATCHBACK = 2
    WAGON = 3

    @classmethod
    def value_of(cls, value: 'CarBodyType') -> 'CarBodyType':
        """
        Return an enum object for the entered string
        """
        for k, v in cls.__members__.items():
            if k == value:
                return v
        else:
            raise ValueError(f"'{cls.__name__}' enum not found for '{value}'")
