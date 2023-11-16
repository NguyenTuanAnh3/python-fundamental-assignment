from classes.park import Park
from classes.pickup import PickUp
from datetime import datetime

def park_option():
    arrival_time = datetime.now().replace(second=0, microsecond=0).strftime("%Y-%m-%d %H:%M")
    try:
        car_identity = input('Enter your car identity: ').strip()
        frequent_parking_number = input('Enter your frequent parking number (if so): ')
        frequent_parking_number = None if frequent_parking_number == '' else int(frequent_parking_number)
    except ValueError:
        print("OOPS, something went wrong!")
    else:
        cus = Park(car_identity=car_identity, arrival_time=arrival_time, frequent_parking_number=frequent_parking_number)
        cus.save_customer_information()

def pickup_option(data):
    enter_car_identity = input("Please enter your car identity: ") 
    leave_day = datetime.now().replace(second=0, microsecond=0).strftime("%Y-%m-%d %H:%M")
    pick_up = PickUp(car_identity=enter_car_identity, leave_day=leave_day)
    pick_up.calculate_fee_parking(data)
