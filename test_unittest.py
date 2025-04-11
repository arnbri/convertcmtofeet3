import unittest
from cm_converter import convert_cm_to_feet

class TestUnitTest(unittest.TestCase):
    def test_tests_work(self):
        self.assertEqual(1+1, 2)

    def test_cm_converter_happy(self):
        self.assertEqual(convert_cm_to_feet(1), 0.0328)
        self.assertEqual(convert_cm_to_feet(0), 0)

    def test_cm_converter_unhappy(self):
        self.assertNotEqual(convert_cm_to_feet(-1), -0.0328, "Cannot convert negative measurements")


if __name__ == "__main__":
    unittest.main()