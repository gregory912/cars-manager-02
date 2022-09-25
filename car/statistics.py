from statistics import mean


class CarStatistics:

    def __init__(self, values: list):
        self.values = values

    def min_value(self):
        """
        The function returns the minimum value from the price list
        """
        return min(self.values)

    def average_value(self):
        """
        The function returns the average value from the price list
        """
        return round(mean(self.values), 2)

    def max_value(self):
        """
        The function returns the maximum value from the price list
        """
        return max(self.values)

    @property
    def get_min_avg_max(self) -> tuple[int, float, int]:
        return self.min_value(), self.average_value(), self.max_value()
