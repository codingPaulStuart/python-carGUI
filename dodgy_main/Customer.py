# Customer Class for storing and moving Data in the GUI Dodgy Bros
# Paul Stuart
# 26.4.21


class Customer:
    def __init__(self, cust_name, cust_phone, vehicle_price, less_trade, sub_amount, gst_amount,
                 final_amount, warranty, window_tint, duco_paint, gps_nav, delux_sound, insurance,
                 under_25, over_25, extras_total):
        self.__cust_name = cust_name
        self.__cust_phone = cust_phone
        self.__vehicle_price = vehicle_price
        self.__less_trade = less_trade
        self.__sub_amount = sub_amount
        self.__gst_amount = gst_amount
        self.__final_amount = final_amount
        self.__warranty = warranty
        self.__window_tint = window_tint
        self.__duco_paint = duco_paint
        self.__gps_nav = gps_nav
        self.__delux_sound = delux_sound
        self.__insurance = insurance
        self.__under_25 = under_25
        self.__over_25 = over_25
        self.__extras_total = extras_total

    def __int__(self):
        self.__cust_name = "Default Name"
        self.__cust_phone = "Default Number"
        self.__vehicle_price = 0
        self.__less_trade = 0
        self.__sub_amount = 0
        self.__gst_amount = 0
        self.__final_amount = 0
        self.__warranty = 0
        self.__window_tint = False
        self.__duco_paint = False
        self.__gps_nav = False
        self.__delux_sound = False
        self.__insurance = 0
        self.__under_25 = False
        self.__over_25 = False
        self.__extras_total = 0

    # GETTERS/SETTERS Personal Details
    def get_cust_name(self):
        return self.__cust_name

    def set_cust_name(self, x):
        self.__cust_name = x

    def get_cust_phone(self):
        return self.__cust_phone

    def set_cust_phone(self, x):
        self.__cust_phone = x

    # GETTERS/SETTERS Financial Details
    def get_vehicle_price(self):
        return self.__vehicle_price

    def set_vehicle_price(self, x):
        self.__vehicle_price = int(x)

    def get_trade(self):
        return self.__less_trade

    def set_trade_in(self, x):
        self.__less_trade = int(x)

    def get_sub_amount(self):
        return self.__sub_amount

    def set_sub_amount(self, x):
        self.__sub_amount = int(x)

    def get_gst_amount(self):
        return self.__gst_amount

    def set_gst_amount(self, x):
        self.__gst_amount = int(x)

    def get_final(self):
        return self.__final_amount

    def set_final(self, x):
        self.__final_amount = int(x)

    # GETTERS/SETTERS Extras Details
    def set_warranty(self, x):
        self.__warranty = x

    def get_warranty(self):
        return self.__warranty

    def set_window(self, x):
        self.__window_tint = x

    def get_window(self):
        return self.__window_tint

    def set_paint(self, x):
        self.__duco_paint = x

    def get_paint(self):
        return self.__duco_paint

    def set_nav(self, x):
        self.__gps_nav = x

    def get_nav(self):
        return self.__gps_nav

    def set_sound(self, x):
        self.__delux_sound = x

    def get_sound(self):
        return self.__delux_sound

    def set_insurance(self, x):
        self.__insurance = x

    def get_insurance(self):
        return self.__insurance

    def set_under25(self, x):
        self.__under_25 = x

    def get_under25(self):
        return self.__under_25

    def set_over25(self, x):
        self.__over_25 = x

    def get_over25(self):
        return self.__over_25

    def set_extras_total(self, x):
        self.__extras_total = int(x)

    def get_extras_total(self):
        return self.__extras_total

    # Calculate Final Amount
    def calculate_final_amount(self):
        sub_total = self.calculate_sub_amount()
        warranty = self.calculate_warranty()
        extras = self.calculate_extras()
        gst = self.calculate_gst()

        final_amount = sub_total + warranty + extras + gst
        self.set_final(int(final_amount))
        return final_amount

    # Calculate Sub Amount
    def calculate_sub_amount(self):
        vehicle_cost = int(self.get_vehicle_price())
        trade_in = int(self.get_trade())
        total = vehicle_cost - trade_in
        self.set_sub_amount(int(total))
        return total

    # Calculate GST
    def calculate_gst(self):
        gst_amount = 0.1 * int(self.get_vehicle_price())
        self.set_gst_amount(int(gst_amount))
        return gst_amount

    # Calculate Extras Amount
    def calculate_extras(self):
        window = self.get_window()
        paint = self.get_paint()
        gps = self.get_nav()
        sound = self.get_sound()
        total = self.get_extras_total()

        if window:
            if True:
                window_cost = 150
                total = total + window_cost
                self.set_extras_total(total)
        if paint:
            if True:
                duco_protection = 180
                total = total + duco_protection

                self.set_extras_total(total)
        if gps:
            if True:
                gps_nav = 320
                total = total + gps_nav

                self.set_extras_total(total)
        if sound:
            if True:
                sound_delux = 350
                total = total + sound_delux
                self.set_extras_total(total)
        else:
            return total

    # Calculate Insurance Amount
    def calculate_insurance(self):
        vehicle_cost = int(self.get_vehicle_price())
        extras = int(self.get_extras_total())

        if self.get_under25():
            if True:
                final = 0.1 * (vehicle_cost + extras)
                return final
        elif self.__over_25():
            if True:
                final = 0.2 * (vehicle_cost + extras)
                return final
        else:
            return 0

    # Calculate Warranty Amount
    def calculate_warranty(self):
        warranty_year = int(self.get_warranty())
        vehicle_cost = int(self.get_vehicle_price())
        if warranty_year == 1:
            return 0
        elif warranty_year == 2:
            warranty = 0.05 * vehicle_cost
            return warranty
        elif warranty_year == 3:
            warranty = 0.1 * vehicle_cost
            return warranty
        else:
            warranty = 0.2 * vehicle_cost
            return warranty

    # F String Output
    def print_customer_summary(self):
        return f"Name: {self.__cust_name} \n" \
               f"Phone: {self.__cust_phone} \n\n" \
               f"Optional Extras ---------------------------- \n\n" \
               f"Warranty: {self.__warranty} years\n" \
               f"Window Tint: {self.__window_tint} \n" \
               f"Duco Paint: {self.__duco_paint} \n" \
               f"GPS Nav: {self.__gps_nav} \n" \
               f"Delux Sound: {self.__delux_sound} \n\n" \
               f" --------------------------------------------- \n\n" \
               f"Insurance: {self.__insurance} \n" \
               f"Under 25: {self.__under_25} \n" \
               f"Over 25: {self.__over_25} \n\n" \
               f"Totals -------------------------------------- \n\n" \
               f"Vehicle Price: ${self.__vehicle_price} \n" \
               f"Less Trade-in: ${self.__less_trade} \n" \
               f"Sub Total:$ {self.__sub_amount} \n" \
               f"GST Amount: ${self.__gst_amount} \n" \
               f"Extras Total: ${self.__extras_total} \n\n" \
               f" --------------------------------------------- \n\n" \
               f"Final Amount: ${self.__final_amount} \n"
