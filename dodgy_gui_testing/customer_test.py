# 4PINT Assessment 2 - Paul Stuart 000389223
# Customer Class TESTING CLASS
# 16.06.21

import unittest
from dodgy_main.Customer import Customer

# Checkout Register Object for testing
customer_1 = Customer("Default Name", "Default Number",
                      0, 0, 0, 0, 0, 0,
                      False, False, False, False,
                      0, False, False, 0)


class customer_testing(unittest.TestCase):

    # Retrieve Customer Name
    def test_customer_name(self):
        expected = "Jimmy"
        customer_1.set_cust_name("Jimmy")
        tester = customer_1.get_cust_name()
        self.assertEqual(expected, tester)

    # # Retrieve Customer Phone
    def test_customer_phone(self):
        expected = "0432567890"
        customer_1.set_cust_phone("0432567890")
        tester = customer_1.get_cust_phone()
        self.assertEqual(expected, tester)

    # Retrieve Vehicle Price
    def test_vehicle_price(self):
        expected = 21000
        customer_1.set_vehicle_price(21000)
        tester = customer_1.get_vehicle_price()
        self.assertEqual(expected, tester)

    # Retrieve Vehicle Trade In
    def test_trade(self):
        expected = 1350
        customer_1.set_trade_in(1350)
        tester = customer_1.get_trade()
        self.assertEqual(expected, tester)

    # Test the sub amount function (veh cost - trade in)
    def test_sub_calculate(self):
        expected = 13650
        customer_1.set_trade_in(1350)
        customer_1.set_vehicle_price(15000)
        tester = customer_1.calculate_sub_amount()
        self.assertEqual(expected, tester)

    # Test the GST amount function (veh cost * 0.1)
    def test_gst_calculate(self):
        expected = 1500
        customer_1.set_vehicle_price(15000)
        tester = customer_1.calculate_gst()
        self.assertEqual(expected, tester)

    # Test Calculate Extras Function
    def test_calc_extras(self):
        expected = 1000
        customer_1.set_sound(True)
        customer_1.set_paint(True)
        customer_1.set_nav(True)
        customer_1.set_window(True)
        customer_1.calculate_extras()
        tester = customer_1.get_extras_total()
        self.assertEqual(expected, tester)

    # Test Warranty for 3 years at 10%
    def test_warranty(self):
        customer_1.set_vehicle_price(15000)
        customer_1.set_warranty(3)
        expected = 1500
        tester = customer_1.calculate_warranty()
        self.assertEqual(expected, tester)

    # Test Warranty for 5 years at 20%
    def test_warranty_2(self):
        customer_1.set_vehicle_price(15000)
        customer_1.set_warranty(5)
        expected = 3000
        tester = customer_1.calculate_warranty()
        self.assertEqual(expected, tester)

    # Test Calculate Total
    def test_total_calc(self):
        customer_1.set_vehicle_price(23000)  # GST should be $2300
        customer_1.set_warranty(2)  # 2 Year Warranty should be $1150
        customer_1.set_trade_in(1700)  # Sub Amount should be $21300
        customer_1.set_nav(True)  # $320
        customer_1.set_paint(True)  # $180
        customer_1.set_window(True)  # $150
        expected = 25400
        customer_1.calculate_final_amount()
        tester = customer_1.get_final()
        self.assertEqual(expected, tester)


if __name__ == '__main__':
    unittest.main()
