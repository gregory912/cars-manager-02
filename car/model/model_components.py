from dataclasses import dataclass
from .model_enums import *
from car.validator import *


@dataclass
class Engine:
    type: EngineType
    power: float

    def __post_init__(self):
        """
        Check that the elements enum are in the correct format
        """
        self.type = EngineType.value_of(self.type) if not isinstance(self.type, EngineType) else self.type


@dataclass
class Wheel:
    model: str
    size: int
    type: TyreType

    def __post_init__(self):
        """
        Check that the elements enum are in the correct format
        """
        self.type = TyreType.value_of(self.type) if not isinstance(self.type, TyreType) else self.type


@dataclass
class CarBody:
    color: CarBodyColor
    type: CarBodyType
    components: list

    def __post_init__(self):
        """
        Check that the elements enum are in the correct format
        """
        self.color = CarBodyColor.value_of(self.color) if not isinstance(self.color, CarBodyColor) else self.color
        self.type = CarBodyType.value_of(self.type) if not isinstance(self.type, CarBodyType) else self.type
        if not validate_components(" ".join(self.components)):
            raise ValueError("The entered components are invalid.")
