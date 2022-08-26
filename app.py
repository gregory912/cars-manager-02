from car.service import CarsService


def main():
    directory = r'data/'
    cars_service = CarsService(directory)


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e.args[0])
