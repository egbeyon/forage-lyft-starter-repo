from tyre.tyre import Tyre
from utils import add_years_to_date


class CarriganTyre(Tyre):
    def __init__(self, wear_array):
        self.wear_array = wear_array

    def needs_service(self):
        for i in self.wear_array:
            if i >= 0.9:
                return True
            else:
                pass
        return False
