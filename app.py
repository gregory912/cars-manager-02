from car.service import CarsService
from data_loader.json import get_cars


def main():
    directory = r'data/'
    cars = get_cars(directory)
    CarsService(cars)


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e.args[0])
