from classes.park import Park
from classes.pickup import PickUp
from create_excel import create_excel
from datetime import datetime


def park_option():
    arrival_time = datetime.now().replace(second=0, microsecond=0).strftime("%Y-%m-%d %H:%M")
    try:
        if(0 <= datetime.strptime(arrival_time, '%Y-%m-%d %H:%M').hour < 8):
            raise Exception("CÚT!!!!")
        car_identity = input('Enter your car identity: ').strip()
        frequent_parking_number = input('Enter your frequent parking number (if so): ')
        frequent_parking_number = None if frequent_parking_number == '' else int(frequent_parking_number)
    except ValueError:
        print("OOPS, something went wrong!")
    except Exception as e:
        print(e)
    else:
        cus = Park(car_identity=car_identity, arrival_time=arrival_time, frequent_parking_number=frequent_parking_number)
        cus.save_customer_information()

def pickup_option(data):
    enter_car_identity = input("Please enter your car identity: ") 
    leave_day = datetime.now().replace(day=17, hour= 20, minute=00, second=0, microsecond=0).strftime("%Y-%m-%d %H:%M")
    pick_up = PickUp(car_identity=enter_car_identity, leave_day=leave_day)
    [bills, total] = pick_up.calculate_fee_parking(data)
    create_excel(car_identity=pick_up.car_identity,leave_day=leave_day, bills=bills)
    print(f'Total payment: {total}')
    print(f'Available Credits: {pick_up.get_available_credit()}')
    while(pick_up.available_creadit < total):
        print("Your a payment amount not enough")
        enter_credit = float(input("Please enter a payment amount:"))
        pick_up.set_available_credit(enter_credit)
        pick_up.save_customer_credit()
        
    if(pick_up.available_creadit >= total):
        pick_up.done_payment(total)
        

    
