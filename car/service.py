from data_loader.json import get_cars


class CarsService:
    def __init__(self, directory: str):
        self.cars = get_cars(directory)
