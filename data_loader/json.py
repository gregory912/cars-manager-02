from car.model.model import Car
import json
import os


def get_cars(directory: str) -> list:
    """
    Get data from json files and return list of Car objects
    """
    cars = []
    for filename in os.listdir(directory):
        with open(directory + filename, 'r') as json_file:
            json_data = json.load(json_file)
            cars.append(Car(json_data, filename))
    return cars
