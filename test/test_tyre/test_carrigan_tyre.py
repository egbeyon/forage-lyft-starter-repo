import unittest

from tyre.carrigan import CarriganTyre


class TestOctoprimeTyre(unittest.TestCase):
    def test_needs_service_true(self):
        wear_array = [0, 0.2, 0.9, 1]
        tyre = OctoprimeTyre(wear_array)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        wear_array = [0, 0.2, 0.7, 0.8]
        tyre = OctoprimeTyre(wear_array)
        self.assertTrue(engine.needs_service())