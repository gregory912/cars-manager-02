from dataclasses import dataclass
from .model_enums import *
from car.validator import *
from typing import Any


@dataclass
class Engine:
    type: EngineType
    power: float

    @classmethod
    def get_model(cls, data: [str, Any]) -> 'Engine':
        """Return properly formatted data"""
        return Engine(
            EngineType.value_of(data['type']) if not isinstance(data['type'], EngineType) else data['type'],
            data['power'])

    def __post_init__(self):
        """
        Check that the elements enum are in the correct format
        """
        if not validate_greater_than_0(self.power):
            raise ValueError("The entered power is incorrect.")


@dataclass
class Wheel:
    model: str
    size: int
    type: TyreType

    @classmethod
    def get_model(cls, data: [str, Any]) -> 'Wheel':
        """Return properly formatted data"""
        return Wheel(
            data['model'],
            data['size'],
            TyreType.value_of(data['type']) if not isinstance(data['type'], TyreType) else data['type'])

    def __post_init__(self):
        """
        Check that the elements enum are in the correct format
        """
        if not validate_model(self.model):
            raise ValueError("The entered model is invalid.")
        if not validate_greater_than_0(self.size):
            raise ValueError("The entered size is incorrect.")


@dataclass
class CarBody:
    color: CarBodyColor
    type: CarBodyType
    components: list

    @classmethod
    def get_model(cls, data: [str, Any]) -> 'CarBody':
        """Return properly formatted data"""
        return CarBody(
            CarBodyColor.value_of(data['color']) if not isinstance(data['color'], CarBodyColor) else data['color'],
            CarBodyType.value_of(data['type']) if not isinstance(data['type'], CarBodyType) else data['type'],
            data['components'])

    def __post_init__(self):
        """
        Check that the elements enum are in the correct format
        """
        if not validate_components(" ".join(self.components)):
            raise ValueError("The entered components are invalid.")
