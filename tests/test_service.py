from car.service import CarsService
from car.model.model import Car
from car.model.model_enums import TyreType


class TestService:
    cars_obj = CarsService(r'tests/test_data/')

    def test_sort_cars(self):
        """
        Test if the function sorts the data properly
        """
        engine_power_true = self.cars_obj.sort_cars("engine.power", True)
        engine_power_false = self.cars_obj.sort_cars("engine.power", False)
        wheel_size_true = self.cars_obj.sort_cars("wheel.size", True)
        wheel_size_false = self.cars_obj.sort_cars("wheel.size", False)
        components_true = self.cars_obj.sort_cars("components", True)
        components_false = self.cars_obj.sort_cars("components", False)

        assert engine_power_true[0].engine.power == 300
        assert engine_power_false[0].engine.power == 100

        assert wheel_size_true[0].wheel.size == 19
        assert wheel_size_false[0].wheel.size == 15

        assert components_true[0].car_body.components == [
            "ANDROID AUTO",
            "ROOF RACK",
            "LEATHER UPHOLSTERY",
            "PANORAMIC ROOF"
        ]
        assert components_false[0].car_body.components == [
            "ABS",
            "AIR CONDITIONING"
        ]

    def test_car_body_with_entered_price(self):
        """
        Test whether the function returns collections of cars with a specific body type and price range
        """
        single_sedan = self.cars_obj.car_body_with_entered_price("SEDAN", 900, 1100)
        two_sedans = self.cars_obj.car_body_with_entered_price("SEDAN", 900, 3100)
        empty = self.cars_obj.car_body_with_entered_price("WAGON", 900, 3100)

        assert single_sedan[0].price == 1000

        assert two_sedans[0].price == 1000
        assert two_sedans[1].price == 3000

        assert not empty

    def test_sorted_cars_with_entered_engine_type(self):
        """
        Test if the function returns a sorted collection of cars with the specified engine type
        """
        diesel_cars = self.cars_obj.sorted_cars_with_entered_engine_type("DIESEL")
        gasoline_cars = self.cars_obj.sorted_cars_with_entered_engine_type("GASOLINE")

        assert diesel_cars[0].model == "AUDI"
        assert diesel_cars[1].model == "MAZDA"

        assert gasoline_cars[0].model == "BMW"
        assert len(gasoline_cars) == 1

    def test_statistics_of_cars(self):
        """
        Test if the function returns correct statistics for price, mileage, power
        """
        price_statistics = self.cars_obj.statistics_of_cars("price")
        mileage_statistics = self.cars_obj.statistics_of_cars("mileage")
        power_statistics = self.cars_obj.statistics_of_cars("power")

        assert price_statistics == (1000, 2000, 3000)
        assert mileage_statistics == (1000, 2000, 3000)
        assert power_statistics == (100.0, 200.0, 300.0)

    def test_mileage_sorted_descending(self):
        """
        Check if the method returns dict in which
        the key is an object of class Car and the value is mileage.
        The pairs should be sorted in descending order of value
        """
        mileage_sorted = self.cars_obj.mileage_sorted_descending()

        assert list(mileage_sorted.items())[0][1] == 3000
        assert isinstance(list(mileage_sorted.items())[0][0], Car)
        assert list(mileage_sorted.values()) == ([3000, 2000, 1000])

    def test_list_of_cars_with_given_tire(self):
        """
        Check if the method returns a dict where the key is the type of tire and
        the value is a list of cars with this type of tire. Dict is sorted in descending
        order by the number of items in the collection.
        """
        tires_dict = self.cars_obj.list_of_cars_with_given_tire()

        assert len(tires_dict) == 2
        assert list(tires_dict.items())[0][0] == TyreType.WINTER
        assert list(tires_dict.items())[1][0] == TyreType.SUMMER

        assert len(list(tires_dict.items())[0][1]) == 2
        assert len(list(tires_dict.items())[1][1]) == 1

    def test_return_cars_that_have_entered_components(self):
        """
        Check if the method returns a collection of cars that have
        all components from the collection passed as an argument.
        The collection is sorted alphabetically by car model name.
        """
        single_component = self.cars_obj.return_cars_that_have_entered_components(["ABS"])
        few_components = self.cars_obj.return_cars_that_have_entered_components(["ANDROID AUTO", "ROOF RACK"])

        assert len(single_component) == 2
        assert single_component[0].car_body.components == ["ABS", "AIR CONDITIONING"]
        assert single_component[1].car_body.components == ["ABS", "CRUISE CONTROL", "ANDROID AUTO"]

        assert len(few_components) == 1
        assert few_components[0].car_body.components == [
            "ANDROID AUTO",
            "ROOF RACK",
            "LEATHER UPHOLSTERY",
            "PANORAMIC ROOF"
        ]
