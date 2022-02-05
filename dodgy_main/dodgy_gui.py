import sqlite3
from datetime import datetime
import tkinter as tk
from tkinter import *
from tkinter import messagebox

from openpyxl import Workbook
from tkcalendar import *
from Customer import Customer


class dodgy_bros:

    @classmethod
    def dodgy_interface(cls):
        # Class to hold the data1 for calculating
        customer_data_1 = Customer("Default Name", "Default Number",
                                   1, 1, 1, 1, 1, 1,
                                   False, False, False, False,
                                   1, False, False, 1)

        # Save the Customer Object instance and call the save Database Function ----------------------------------------
        def save_customer():
            customer_data_1.set_cust_name(left_col_cust_nameEn.get())
            customer_data_1.set_cust_phone(left_col_cust_phoneEn.get())
            customer_data_1.set_vehicle_price(int(left_col_vehiclePEn.get()))
            customer_data_1.set_trade_in(int(left_col_vehicleTrEn.get()))

            # Convert Warranty Option to value
            warranty_final = warranty_value.get()
            if warranty_final == '1-year 0%':
                customer_data_1.set_warranty(1)
            elif warranty_final == '2-year 5%':
                customer_data_1.set_warranty(2)
            elif warranty_final == '3-year 10%':
                customer_data_1.set_warranty(3)
            else:
                customer_data_1.set_warranty(5)

            # Central Panel - Extras --- Widgets return 0 or 1 then convert to booleans for the Customer Class
            window = check_var_window.get()
            paint = check_var_paint.get()
            sound = check_var_sound.get()
            gps = check_var_gps.get()

            if window == 1:
                customer_data_1.set_window(True)
            else:
                customer_data_1.set_window(False)

            if paint == 1:
                customer_data_1.set_paint(True)
            else:
                customer_data_1.set_paint(False)

            if sound == 1:
                customer_data_1.set_sound(True)
            else:
                customer_data_1.set_sound(False)

            if gps == 1:
                customer_data_1.set_nav(True)
            else:
                customer_data_1.set_nav(False)

            # Run the class functions to process totals
            customer_data_1.calculate_sub_amount()
            customer_data_1.calculate_gst()
            customer_data_1.calculate_final_amount()

            # Fill in the Sub, GST and Final Amounts in GUI
            left_col_subEn.insert(END, customer_data_1.calculate_sub_amount())
            left_col_gstEn.insert(END, customer_data_1.calculate_gst())
            left_col_finEn.insert(END, customer_data_1.calculate_final_amount())

            # Call the database Write to Function once all the above has been completed
            save_database()
            right_col_text_summary.insert(END, "\nDetails saved to Customer Object and write to DB method called\n")

        # Reset the Customer so all the values are default -------------------------------------------------------------
        def reset_customer():
            # Reset the Customer Data Object Instance
            customer_data_1.set_cust_name("None")
            customer_data_1.set_cust_phone("None")
            customer_data_1.set_vehicle_price(0)
            customer_data_1.set_extras_total(0)
            customer_data_1.set_warranty(0)
            customer_data_1.set_nav(False)
            customer_data_1.set_gst_amount(0)
            customer_data_1.set_insurance(0)
            customer_data_1.set_over25(False)
            customer_data_1.set_paint(False)
            customer_data_1.set_sound(False)
            customer_data_1.set_under25(False)
            customer_data_1.set_trade_in(0)
            customer_data_1.set_sub_amount(0)
            customer_data_1.set_window(False)
            customer_data_1.set_final(0)

            # Reset the Text Field Boxes
            right_col_text_summary.delete(1.0, END)
            left_col_cust_nameEn.delete(0, END)
            left_col_cust_phoneEn.delete(0, END)
            left_col_vehiclePEn.delete(0, END)
            left_col_vehicleTrEn.delete(0, END)
            left_col_subEn.delete(0, END)
            left_col_gstEn.delete(0, END)
            left_col_finEn.delete(0, END)
            check_var_sound.set(0)
            check_var_paint.set(0)
            check_var_gps.set(0)
            check_var_window.set(0)
            warranty_value.set(warranty_list[0])
            print("Fields have been reset")

        # Get the F String method from the Object instance and output to the Summary Screen ----------------------------
        def summary_result():
            right_col_text_summary.insert(END, str(datetime.now()) + "\n\n")
            right_col_text_summary.insert(END, customer_data_1.print_customer_summary())
            right_col_text_summary.insert(END, "\nCustomer Print Method called from class and inserted\n")

        # Retrieve Database entries and open in Excel File -------------------------------------------------------------
        def open_excel_results():
            conn = sqlite3.connect('dodgyDB.db')
            select_sql = '''SELECT * FROM customer_table;'''
            data_set = conn.execute(select_sql)
            dodgy_wb = Workbook()
            sheet = dodgy_wb.active
            row_headers = ["Customer Name", "Phone Number", "GST Total", "Final Amount"]

            sheet.append(row_headers)
            for _ in data_set:
                sheet.append(_)
            dodgy_wb.save("dodgy_list.xlsx")
            right_col_text_summary.insert(END, "\nExcel File written to in Directory - 'dodgy_list.xlsx' \n")

        # Save to the Database, write the object instance --------------------------------------------------------------
        def save_database():
            # Run the Database connection to SQL Lite
            try:
                create_table_sql = '''CREATE TABLE IF NOT EXISTS customer_table (
                                 Name text NOT NULL,
                                 Phone int PRIMARY KEY NOT NULL,
                                 GstAmount decimal(10,2),
                                 FinalAmount float);'''

                conn = sqlite3.connect('dodgyDB.db')
                cursor = conn.cursor()
                cursor.execute(create_table_sql)

                Name = customer_data_1.get_cust_name()
                Phone = customer_data_1.get_cust_phone()
                GSTAmount = customer_data_1.get_gst_amount()
                FinalAmount = customer_data_1.get_final()

                customer_record = [Name, Phone, GSTAmount, FinalAmount]

                insert_table_sql = '''INSERT INTO customer_table (Name, Phone, GstAmount, FinalAmount)
                            VALUES (?,?,?,?);'''

                cursor = conn.execute(insert_table_sql, customer_record)
                messagebox.showinfo("Dodgy DB", "Records Saved to Car Dealer DB")
                cursor.close()
                conn.commit()

            except Exception as e:
                conn.rollback()
                print("Transaction Rolled Back")

            finally:
                conn.close()
            right_col_text_summary.insert(END, "\nCustomer Details Written to Database\n")

        # GUI and Grid starts here -------------------------------------------------------------------------------------
        PADDING_BIG = 7
        PADDING_SMALL = 3
        PADDING_MED = 6
        BACKGROUND_COL = 'yellow'
        BACKGROUND_COL2 = 'LightCyan2'
        SUB_HEAD_COL = 'gray46'
        ENTRY_WIDTH = 30
        HEAD_FONT_1 = 14
        HEAD_FONT_2 = 10
        BODY_FONT_MED = 10
        BODY_FONT_SM = 8

        gui_root = tk.Tk()
        gui_root.geometry('1150x700')
        gui_root.winfo_toplevel().title('Dodgy Bros Car Dealers')
        gui_root.iconbitmap('carYellow.ico')
        gui_root.configure(bg=BACKGROUND_COL)
        gui_root.columnconfigure(0, weight=1)
        gui_root.columnconfigure(1, weight=1)
        gui_root.columnconfigure(2, weight=1)

        # Top Row and Header -------------------------------------------------------------------------------------------
        top_header = tk.Label(gui_root, text="Dodgy Brothers Car Dealers", bg=BACKGROUND_COL, fg='gray25',
                              font=('Tahoma', 28))
        top_header.grid(column=0, row=0, columnspan=3, ipadx=PADDING_MED, ipady=PADDING_MED, sticky="NSEW")

        # Left Column --------------------------------------------------------------------------------------------------

        # Calc Sub Head
        left_col = tk.Label(gui_root, text="Customer Details", bg=BACKGROUND_COL, fg=SUB_HEAD_COL,
                            font=('Tahoma', HEAD_FONT_1, 'bold'))
        left_col.grid(column=0, row=1, padx=(20, 5), pady=PADDING_MED, sticky="W")

        # Customer Name Widgets
        left_col_cust_nameLb = tk.Label(gui_root, justify='right', text="Cust Name", bg=BACKGROUND_COL,
                                        font=('Tahoma', BODY_FONT_MED))
        left_col_cust_nameLb.grid(column=0, row=2, pady=PADDING_SMALL, padx=(40, 2), sticky='W')
        left_col_cust_nameEn = tk.Entry(gui_root, justify='left', width=ENTRY_WIDTH, bg=BACKGROUND_COL2)
        left_col_cust_nameEn.grid(column=0, row=2, pady=PADDING_SMALL, padx=(0, 40), sticky='E')

        # Customer Phone Widgets
        left_col_cust_phoneLb = tk.Label(gui_root, justify='right', text="Cust Phone", bg=BACKGROUND_COL,
                                         font=('Tahoma', BODY_FONT_MED))
        left_col_cust_phoneLb.grid(column=0, row=3, pady=PADDING_SMALL, padx=(40, 2), sticky='W')
        left_col_cust_phoneEn = tk.Entry(gui_root, justify='left', width=ENTRY_WIDTH, bg=BACKGROUND_COL2)
        left_col_cust_phoneEn.grid(column=0, row=3, pady=PADDING_SMALL, padx=(0, 40), sticky='E')

        # Vehicle Price Widgets
        left_col_vehiclePLb = tk.Label(gui_root, justify='right', text="Veh Price", bg=BACKGROUND_COL,
                                       font=('Tahoma', BODY_FONT_MED))
        left_col_vehiclePLb.grid(column=0, row=4, pady=PADDING_SMALL, padx=(40, 2), sticky='W')
        left_col_vehiclePEn = tk.Entry(gui_root, justify='left', width=ENTRY_WIDTH, bg=BACKGROUND_COL2)
        left_col_vehiclePEn.grid(column=0, row=4, pady=PADDING_SMALL, padx=(0, 40), sticky='E')

        # Vehicle Trade Widgets
        left_col_vehicleTrLb = tk.Label(gui_root, justify='right', text="Less Trade", bg=BACKGROUND_COL,
                                        font=('Tahoma', BODY_FONT_MED))
        left_col_vehicleTrLb.grid(column=0, row=5, pady=PADDING_SMALL, padx=(40, 2), sticky='W')
        left_col_vehicleTrEn = tk.Entry(gui_root, justify='left', width=ENTRY_WIDTH, bg=BACKGROUND_COL2)
        left_col_vehicleTrEn.grid(column=0, row=5, pady=PADDING_SMALL, padx=(0, 40), sticky='E')

        # Calc Sub Head
        left_col = tk.Label(gui_root, text="Calculations", bg=BACKGROUND_COL, fg=SUB_HEAD_COL,
                            font=('Tahoma', HEAD_FONT_1, 'bold'))
        left_col.grid(column=0, row=6, padx=(20, 5), pady=PADDING_BIG, sticky="W")

        # Sub Amount Widgets
        left_col_subLb = tk.Label(gui_root, justify='right', text="Sub amount", bg=BACKGROUND_COL,
                                  font=('Tahoma', BODY_FONT_MED))
        left_col_subLb.grid(column=0, row=7, pady=PADDING_SMALL, padx=(40, 2), sticky='W')
        left_col_subEn = tk.Entry(gui_root, justify='left', width=ENTRY_WIDTH, bg=BACKGROUND_COL2)
        left_col_subEn.grid(column=0, row=7, pady=PADDING_SMALL, padx=(0, 40), sticky='E')

        # GST Amount Widgets
        left_col_gstLb = tk.Label(gui_root, justify='right', text="GST amount", bg=BACKGROUND_COL,
                                  font=('Tahoma', BODY_FONT_MED))
        left_col_gstLb.grid(column=0, row=8, pady=PADDING_SMALL, padx=(40, 2), sticky='W')
        left_col_gstEn = tk.Entry(gui_root, justify='left', width=ENTRY_WIDTH, bg=BACKGROUND_COL2)
        left_col_gstEn.grid(column=0, row=8, pady=PADDING_SMALL, padx=(0, 40), sticky='E')

        # Final Amount Widgets
        left_col_finLb = tk.Label(gui_root, justify='right', text="Final amount", bg=BACKGROUND_COL,
                                  font=('Tahoma', BODY_FONT_MED))
        left_col_finLb.grid(column=0, row=9, pady=PADDING_SMALL, padx=(40, 2), sticky='W')
        left_col_finEn = tk.Entry(gui_root, justify='left', width=ENTRY_WIDTH, bg=BACKGROUND_COL2)
        left_col_finEn.grid(column=0, row=9, pady=PADDING_SMALL, padx=(0, 40), sticky='E')

        # Central Sub Head (Collection)
        central_col2_collect = tk.Label(gui_root, text="Collection", bg=BACKGROUND_COL, fg=SUB_HEAD_COL,
                                        font=('Tahoma', HEAD_FONT_1, 'bold'))
        central_col2_collect.grid(column=0, row=10, padx=(20, 5), pady=PADDING_SMALL, sticky="W")

        # Date Picker
        central_col2_date = Calendar(gui_root, selectmode="day", year=2021, month=6, day=1)
        central_col2_date.grid(column=0, row=11, padx=(45, 2), pady=20, sticky="W")

        # Central Column -----------------------------------------------------------------------------------------------

        # Central Sub Head (Extras)
        central_col = tk.Label(gui_root, text="Warranty", bg=BACKGROUND_COL, fg=SUB_HEAD_COL,
                               font=('Tahoma', HEAD_FONT_1, 'bold'))
        central_col.grid(column=1, row=1, padx=PADDING_SMALL, pady=PADDING_MED, sticky="W")

        # Vehicle Warranty Drop Down
        warranty_list = ['1-year 0%', '2-year 5%', '3-year 10%', '5-year 20%']
        warranty_value = StringVar(gui_root)
        warranty_value.set(warranty_list[0])
        cen_col_warrantyDD = tk.OptionMenu(gui_root, warranty_value, *warranty_list)
        cen_col_warrantyDD.configure(width=ENTRY_WIDTH)
        cen_col_warrantyDD.grid(column=1, row=2, padx=(5, 30), pady=PADDING_SMALL, sticky="EW")

        # Central Sub Head (Extras)
        central_col2 = tk.Label(gui_root, text="Optional Extras", bg=BACKGROUND_COL, fg=SUB_HEAD_COL,
                                font=('Tahoma', HEAD_FONT_1, 'bold'))
        central_col2.grid(column=1, row=3, padx=PADDING_SMALL, pady=PADDING_MED, sticky="W")

        # Optional Extras Checkboxes
        check_var_window = IntVar()
        cen_col_check_window = Checkbutton(gui_root, bg=BACKGROUND_COL, font=('Tahoma', BODY_FONT_MED),
                                           text='Window Tint ($150)',
                                           variable=check_var_window, onvalue=1,
                                           offvalue=0)
        cen_col_check_window.grid(column=1, row=4, padx=(20, 5), pady=PADDING_SMALL, sticky="W")

        check_var_paint = IntVar()
        cen_col_check_duco = Checkbutton(gui_root, bg=BACKGROUND_COL, font=('Tahoma', BODY_FONT_MED),
                                         text='Duco Protection (180)',
                                         variable=check_var_paint, onvalue=1,
                                         offvalue=0)
        cen_col_check_duco.grid(column=1, row=5, padx=(20, 5), pady=PADDING_SMALL, sticky="W")

        check_var_gps = IntVar()
        cen_col_check_gps = Checkbutton(gui_root, bg=BACKGROUND_COL, font=('Tahoma', BODY_FONT_MED),
                                        text='GPS Navigation (320)',
                                        variable=check_var_gps, onvalue=1,
                                        offvalue=0)
        cen_col_check_gps.grid(column=1, row=6, padx=(20, 5), pady=PADDING_SMALL, sticky="W")

        check_var_sound = IntVar()
        cen_col_check_sound = Checkbutton(gui_root, bg=BACKGROUND_COL, font=('Tahoma', BODY_FONT_MED),
                                          text='Delux Sound System (350)',
                                          variable=check_var_sound, onvalue=1,
                                          offvalue=0)
        cen_col_check_sound.grid(column=1, row=7, padx=(20, 5), pady=PADDING_SMALL, sticky="W")

        # Central Sub Head (Run the SQL query and save to Excel File)
        central_col2_sql_head = tk.Label(gui_root, text="SQL Database Results", bg=BACKGROUND_COL, fg=SUB_HEAD_COL,
                                         font=('Tahoma', HEAD_FONT_1, 'bold'))
        central_col2_sql_head.grid(column=1, row=8, padx=(20, 5), pady=(10, 5), sticky="W")

        # SQL retrieve Function from Database and open in excel Workbook
        central_col_saveSQLBtn = Button(gui_root, command=open_excel_results,
                                        text="Retrieve Results, save to excel", width=40, fg='black', bg='light green',
                                        font=('Tahoma', HEAD_FONT_2, 'bold'))
        central_col_saveSQLBtn.grid(column=1, row=9, padx=(5, 5), pady=PADDING_SMALL, sticky="W")

        # Image widget of Car
        central_yellow_car = PhotoImage(file='lamborghini-png--1792.png')
        central_image_col_center = Label(gui_root, image=central_yellow_car, bg=BACKGROUND_COL, width=250)
        central_image_col_center.grid(column=1, row=10, rowspan=11, padx=PADDING_SMALL, pady=PADDING_SMALL, sticky="W")

        # Right Column -------------------------------------------------------------------------------------------------

        # Right Sub Head
        right_col = tk.Label(gui_root, text="Summary", bg=BACKGROUND_COL, fg=SUB_HEAD_COL,
                             font=('Tahoma', HEAD_FONT_1, 'bold'))
        right_col.grid(column=2, row=1, padx=PADDING_SMALL, pady=PADDING_MED, sticky="W")

        # Buttons for save, summary and reset (Command functions are called)
        right_col_saveBtn = Button(gui_root, command=save_customer,
                                   text="SAVE", width=30, fg=SUB_HEAD_COL,
                                   font=('Tahoma', HEAD_FONT_2, 'bold'))
        right_col_saveBtn.grid(column=2, row=2, padx=(5, 40), pady=PADDING_SMALL, sticky="EW")

        right_col_sumBtn = Button(gui_root, command=summary_result, text="SUMMARY", width=30, fg=SUB_HEAD_COL,
                                  font=('Tahoma', HEAD_FONT_2, 'bold'))
        right_col_sumBtn.grid(column=2, row=3, padx=(5, 40), pady=PADDING_SMALL, sticky="EW")

        right_col_resetBtn = Button(gui_root, command=reset_customer, text="RESET", width=30, fg=SUB_HEAD_COL,
                                    font=('Tahoma', HEAD_FONT_2, 'bold'))
        right_col_resetBtn.grid(column=2, row=4, padx=(5, 40), pady=PADDING_SMALL, sticky="EW")

        # Text Bod Summary display
        right_col_text_summary = Text(gui_root, width=41, height=30,
                                      padx=10, pady=10, fg=SUB_HEAD_COL,
                                      font=('Tahoma', BODY_FONT_SM, 'bold'))
        right_col_text_summary.grid(column=2, row=5, rowspan=11, padx=(5, 40), pady=PADDING_SMALL, sticky="EW")

        gui_root.mainloop()
