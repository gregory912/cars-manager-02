from car.service import CarsService
from car.model.model_components import *
from data_loader.json import get_cars
from decimal import Decimal


class TestModel:
    cars = get_cars(r'tests/test_data/')
    # cars = get_cars(r'./test_data/')
    cars_obj = CarsService(cars)
    car = cars_obj.cars_obj[0]

    def test_types_of_fields_model(self):
        """
        Test if the model field has correct type
        """
        assert isinstance(self.car.model, str)

    def test_types_of_fields_price(self):
        """
        Test if the price field has correct type
        """
        assert isinstance(self.car.price, Decimal)

    def test_types_of_fields_mileage(self):
        """
        Test if the mileage field has correct type
        """
        assert isinstance(self.car.mileage, int)

    def test_types_of_fields_engine(self):
        """
        Test if the engine field has correct type
        """
        assert isinstance(self.car.engine, Engine)

    def test_types_of_fields_car_body(self):
        """
        Test if the car body field has correct type
        """
        assert isinstance(self.car.car_body, CarBody)

    def test_types_of_fields_wheel(self):
        """
        Test if the wheel field has correct type
        """
        assert isinstance(self.car.wheel, Wheel)

    def test_types_of_fields_engine_type(self):
        """
        Test if the engine type field has correct type
        """
        assert isinstance(self.car.engine.type, EngineType)

    def test_types_of_fields_engine_power(self):
        """
        Test if the engine power field has correct type
        """
        assert isinstance(self.car.engine.power, float)

    def test_types_of_fields_car_body_color(self):
        """
        Test if the carbody color field has correct type
        """
        assert isinstance(self.car.car_body.color, CarBodyColor)

    def test_types_of_fields_car_body_type(self):
        """
        Test if the car body type field has correct type
        """
        assert isinstance(self.car.car_body.type, CarBodyType)

    def test_types_of_fields_car_body_components(self):
        """
        Test if the car body components field has correct type
        """
        assert isinstance(self.car.car_body.components, list)

    def test_types_of_fields_wheel_model(self):
        """
        Test if the wheel model field has correct type
        """
        assert isinstance(self.car.wheel.model, str)

    def test_types_of_fields_wheel_size(self):
        """
        Test if the wheel size field has correct type
        """
        assert isinstance(self.car.wheel.size, int)

    def test_types_of_fields_wheel_type(self):
        """
        Test if the wheel type field has correct type
        """
        assert isinstance(self.car.wheel.type, TyreType)

    def test_has_price_between_in_range(self):
        """
        Test that the has_price_between method returns True for the correct range
        """
        assert self.car.has_price_between(Decimal(900), Decimal(1100))

    def test_has_price_between_out_of_range(self):
        """
        Test if the has_price_between method returns False for an invalid range
        """
        assert not self.car.has_price_between(Decimal(1001), Decimal(1100))

    def test_has_type_correct_value(self):
        """
        Test that the has_type_correct method returns True for the correct type
        """
        assert self.car.has_type(CarBodyType.SEDAN)

    def test_has_type_wrong_value(self):
        """
        Test if the has_type_correct method returns False for the wrong type
        """
        assert not self.car.has_type(CarBodyType.WAGON)

    def test_has_engine_type_correct_value(self):
        """
        Test if the has_engine_type method returns True for the correct type
        """
        assert self.car.has_engine_type(EngineType.DIESEL)

    def test_has_engine_type_wrong_value(self):
        """
        Test if the has_engine_type method returns False for an invalid type
        """
        assert not self.car.has_engine_type(EngineType.GASOLINE)

    def test_is_winter(self):
        """
        Test if the is_winter method returns correct results
        """
        assert self.car.is_winter()

    def test_has_components_with_component(self):
        """
        Test that the has components method returns True for the components that the object has
        """
        assert self.car.has_components(['ABS'])

    def test_has_components_without_component(self):
        """
        Test that the has components method returns False for components that do not have an object
        """
        assert not self.car.has_components(['ANDROID AUTO'])
