from car.service import CarsService
from car.model.model import Car
from car.model.model_enums import *
from car.enums import *
from data_loader.json import get_cars
from decimal import Decimal


class TestService:
    cars = get_cars(r'tests/test_data/')
    cars_obj = CarsService(cars)

    def test_sort_cars_engine_power(self):
        """
        Test if the method correctly sorts elements for engine_power
        """
        engine_power = self.cars_obj.sort_cars(SortType.ENGINE_POWER, False)

        assert engine_power[0].engine.power == 100

    def test_sort_cars_engine_power_desc(self):
        """
        Test that the method correctly sorts descending elements for engine_power
        """
        engine_power_desc = self.cars_obj.sort_cars(SortType.ENGINE_POWER, True)
        assert engine_power_desc[0].engine.power == 300

    def test_sort_cars_wheel_size(self):
        """
        Test if the method correctly sorts elements for wheel size
        """
        wheel_size = self.cars_obj.sort_cars(SortType.WHEEL_SIZE, False)

        assert wheel_size[0].wheel.size == 15

    def test_sort_cars_wheel_size_desc(self):
        """
        Test that the method correctly sorts descending elements for wheel size
        """
        wheel_size_desc = self.cars_obj.sort_cars(SortType.WHEEL_SIZE, True)

        assert wheel_size_desc[0].wheel.size == 19

    def test_sort_cars_components(self):
        """
        Test if the method correctly sorts elements for components
        """
        components = self.cars_obj.sort_cars(SortType.COMPONENTS, False)

        assert components[0].car_body.components == ["ABS", "AIR CONDITIONING"]

    def test_sort_cars_components_desc(self):
        """
        Test that the method correctly sorts descending elements for components
        """
        components_true = self.cars_obj.sort_cars(SortType.COMPONENTS, True)

        assert components_true[0].car_body.components == [
            "ANDROID AUTO",
            "ROOF RACK",
            "LEATHER UPHOLSTERY",
            "PANORAMIC ROOF"
        ]

    def test_car_body_with_entered_price_single_car(self):
        """
        Test whether the function returns collections of cars with a specific body type and price range
        """
        single_sedan = self.cars_obj.get_car_body_with_entered_price(CarBodyType.SEDAN, Decimal(900), Decimal(1100))

        assert single_sedan[0].price == 1000

    def test_car_body_with_entered_price_many_cars(self):
        """
        Test whether the function returns collections of cars with a specific body type and price range
        """
        two_sedans = self.cars_obj.get_car_body_with_entered_price(CarBodyType.SEDAN, Decimal(900), Decimal(3100))

        assert two_sedans[0].price == 1000
        assert two_sedans[1].price == 3000

    def test_car_body_with_entered_price_empty(self):
        """
        Test whether the function returns collections of cars with a specific body type and price range
        """
        empty = self.cars_obj.get_car_body_with_entered_price(CarBodyType.WAGON, Decimal(900), Decimal(3100))

        assert not empty

    def test_sorted_cars_with_entered_engine_type_diesel(self):
        """
        Test that the function returns a sorted collection of diesel cars
        """
        diesel_cars = self.cars_obj.get_sorted_cars_with_entered_engine_type(EngineType.DIESEL)

        assert diesel_cars[0].model == "AUDI"
        assert diesel_cars[1].model == "MAZDA"

    def test_sorted_cars_with_entered_engine_type_gasoline(self):
        """
        Test that the function returns a sorted collection of gasoline cars
        """
        gasoline_cars = self.cars_obj.get_sorted_cars_with_entered_engine_type(EngineType.GASOLINE)

        assert gasoline_cars[0].model == "BMW"
        assert len(gasoline_cars) == 1

    def test_statistics_of_cars_price(self):
        """
        Test if the function returns correct statistics for price
        """
        price_statistics = self.cars_obj.get_statistics_of_cars(Statistic.PRICE)

        assert price_statistics == (1000, 2000, 3000)

    def test_statistics_of_cars_mileage(self):
        """
        Test if the function returns correct statistics for mileage
        """
        mileage_statistics = self.cars_obj.get_statistics_of_cars(Statistic.MILEAGE)

        assert mileage_statistics == (1000, 2000, 3000)

    def test_statistics_of_cars_power(self):
        """
        Test if the function returns correct statistics for power
        """
        power_statistics = self.cars_obj.get_statistics_of_cars(Statistic.POWER)

        assert power_statistics == (100.0, 200.0, 300.0)

    def test_mileage_sorted_descending(self):
        """
        Check if the method returns dict in which
        the key is an object of class Car and the value is mileage.
        The pairs should be sorted in descending order of value
        """
        mileage_sorted = self.cars_obj.get_mileage_sorted_descending()

        assert list(mileage_sorted.items())[0][1] == 3000
        assert isinstance(list(mileage_sorted.items())[0][0], Car)
        assert list(mileage_sorted.values()) == ([3000, 2000, 1000])

    def test_list_of_cars_with_given_tire(self):
        """
        Check if the method returns a dict where the key is the type of tire and
        the value is a list of cars with this type of tire. Dict is sorted in descending
        order by the number of items in the collection.
        """
        tires_dict = self.cars_obj.get_list_of_cars_with_given_tire()

        assert len(tires_dict) == 2
        assert list(tires_dict.items())[0][0] == TyreType.WINTER
        assert list(tires_dict.items())[1][0] == TyreType.SUMMER

        assert len(list(tires_dict.items())[0][1]) == 2
        assert len(list(tires_dict.items())[1][1]) == 1

    def test_return_cars_that_have_entered_components_single_component(self):
        """
        Check if the method returns a collection of cars that have
        all components from the collection passed as an argument.
        The collection is sorted alphabetically by car model name.
        """
        single_component = self.cars_obj.return_cars_that_have_entered_components(["ABS"])

        assert len(single_component) == 2
        assert single_component[0].car_body.components == ["ABS", "AIR CONDITIONING"]
        assert single_component[1].car_body.components == ["ABS", "CRUISE CONTROL", "ANDROID AUTO"]

    def test_return_cars_that_have_entered_components_many_components(self):
        """
        Check if the method returns a collection of cars that have
        all components from the collection passed as an argument.
        The collection is sorted alphabetically by car model name.
        """
        few_components = self.cars_obj.return_cars_that_have_entered_components(["ANDROID AUTO", "ROOF RACK"])

        assert len(few_components) == 1
        assert few_components[0].car_body.components == [
            "ANDROID AUTO",
            "ROOF RACK",
            "LEATHER UPHOLSTERY",
            "PANORAMIC ROOF"
        ]
