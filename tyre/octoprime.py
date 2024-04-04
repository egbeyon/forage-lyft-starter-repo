from tyre.tyre import Tyre
from utils import add_years_to_date


class OctoprimeTyre(Tyre):
    def __init__(self, wear_array):
        self.wear_array = wear_array

    def needs_service(self):
        total = 0
        for i in self.wear_array:
            total += i
        if total >= 3:
            return True
        else:
            return False
