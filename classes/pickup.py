import os
from classes.customer import Customer
import datetime

ARRIVAL_TIME_TEXT  = 'Arrival Time'
CAR_INDENTITY_TEXT = 'Car Identity'
FREQUENT_PARKING_NUMBER_TEXT = 'Frequent Parking Number'
DAY_OF_WEEK = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

class PickUp(Customer):

    global ARRIVAL_TIME_TEXT
    global CAR_INDENTITY_TEXT
    global FREQUENT_PARKING_NUMBER_TEXT
    global DAY_OF_WEEK
    
    def __init__(self, car_identity, leave_day, available_creadit=0.0):
        super().__init__(car_identity, available_creadit)
        self.leave_day = leave_day
        self.info = {}
        self.bill = {}
        self.bills = []

    def get_arrival_day(self):
        try:
            get_arrival_time =  self.get_customer_information()[ARRIVAL_TIME_TEXT].strip()
            arrival_day = datetime.datetime.strptime(get_arrival_time, "%Y-%m-%d %H:%M")
            if(0 <= arrival_day.hour < 8):
                raise Exception("OOPs, arrival time went wrong")
        except Exception as e:
            print(e)
            exit()
        else:
            return arrival_day

    def get_leave_day(self):
        return datetime.datetime.strptime(self.leave_day, "%Y-%m-%d %H:%M")

    def get_range_date(self):
        date = datetime.datetime
        arrival_day = self.get_arrival_day()
        leave_day = self.get_leave_day()
        return [(arrival_day + datetime.timedelta(days=delta)).strftime('%Y-%m-%d') for delta in range((leave_day - arrival_day).days + 1)]
    
    def split_periods_day(self, day):
        day_time = day.replace(hour=16, minute=59)
        night_time = day.replace(hour=23, minute=59)
        new_day = (day + datetime.timedelta(days=1)).replace(hour=8, minute=0)
        return [day_time, night_time, new_day] 

    def get_fee_each_day(self, start_day, end_day, data):
        [day_time, night_time, new_day] = self.split_periods_day(start_day)
        self.bill['date'] = start_day.strftime("%Y-%m-%d")
        self.bill['dayOfWeek'] = DAY_OF_WEEK[start_day.weekday()]
        parking_regulation = data[self.bill['dayOfWeek']]

        for park in parking_regulation:
            temp_str = park['start'] + ' - ' + park['end']
            park['pricePerHour'] = round(park['pricePerHour'], 2)
            if park['start'] == '08:00' and park['end'] == '16:59':
                if (start_day < end_day and end_day < day_time):
                    sub_time = round((end_day - start_day).seconds/3600)
                    time_remain = sub_time - int(park['maxStayInHours'])
                elif(day_time < start_day) :
                    sub_time = 0
                    time_remain = 0
                else:
                    sub_time = round((day_time - start_day).seconds/3600)
                    time_remain = sub_time - int(park['maxStayInHours'])

                self.bill[temp_str] = [
                    {
                        "time": sub_time if sub_time <= 2 else park['maxStayInHours'],
                        "price_per_hour": sub_time if sub_time == 0 else park['pricePerHour'],
                        "str_price_per_hour": '' if sub_time == 0 else f'${"{0:.2f}".format(park["pricePerHour"])}/h' 
                    },
                    {
                        "time": 0 if (sub_time == 0 or time_remain <= 0 ) else time_remain,
                        "price_per_hour": 0 if time_remain <= 0 else park['pricePerHour'] * 2,
                        "str_price_per_hour": '' if time_remain <= 0 else f'${"{0:.2f}".format(park["pricePerHour"])}/h * 2' 
                    }
                ]
            elif park['start'] == '17:00' and park['end'] == '23:59':
                if( day_time < start_day < end_day and end_day < night_time):
                    sub_time = round((end_day - start_day).seconds/3600)
                elif(day_time < start_day):
                    sub_time = round((night_time - start_day).seconds/3600)
                elif(day_time < end_day < night_time):
                    sub_time = round((end_day - day_time).seconds/3600) 
                elif(end_day < day_time):
                    sub_time = 0     
                else:
                    sub_time = round((night_time - day_time).seconds/3600)

                self.bill[temp_str] = [
                {
                    "time": sub_time,
                    "price_per_hour": park['pricePerHour'] if sub_time != 0 else 0,
                    "str_price_per_hour": f'${"{0:.2f}".format(park["pricePerHour"])}/h' if sub_time != 0 else ''
                }
               ]
            else:
                sub_time = 1
                if(end_day < day_time or day_time < end_day < night_time):
                    sub_time = 0
                elif(night_time < start_day < end_day):
                    sub_time = round((end_day - start_day)/3600)

                self.bill[temp_str] = [
                {
                    "time": 'N/A' if sub_time != 0 else 0,
                    "price_per_hour": park['pricePerHour'] if sub_time != 0 else 0,
                    "str_price_per_hour": f'${"{0:.2f}".format(park["pricePerHour"])}' if sub_time != 0 else ''
                }
               ]
        
        return self.bill

    def calculate_sub_total_each_day(self):
        sub_total = 0
        for k, value in self.bill.items():
            if k == 'date' or k == 'dayOfWeek':
                continue
            for v in value:
                if(v['time'] == 'N/A'):
                    sub_total += v['price_per_hour'] 
                else:
                    sub_total += int(v['time']) * v['price_per_hour'] 
        self.bill['sub_total'] = sub_total
        return self.bill

    def get_bills_parking(self, data):
        start_day = self.get_arrival_day()
        end_day = self.get_leave_day()
        range_date = self.get_range_date()
        for index, day in enumerate(range_date):
            day = datetime.datetime.strptime(day, "%Y-%m-%d")
            next_day = (day + datetime.timedelta(days=1)).replace(hour=8, minute=0)
            self.bill = {}
            if index == 0 and len(range_date) > 1:
                self.get_fee_each_day(start_day=start_day, end_day= next_day, data=data)
                self.calculate_sub_total_each_day()
            elif index == 0 and len(range_date) == 1:
                self.get_fee_each_day(start_day=start_day, end_day= end_day, data=data)
                self.calculate_sub_total_each_day()
                self.bills.append(self.bill)
                return self.bills
            elif (index == len(range_date) - 1) :
                previous_time = end_day.replace(hour=8, minute=0)
                self.get_fee_each_day(start_day=previous_time, end_day= end_day, data=data)
                self.calculate_sub_total_each_day()
            else:
                day = day.replace(hour=8, minute=0)
                self.get_fee_each_day(start_day=day, end_day= next_day, data=data)
                self.calculate_sub_total_each_day()
            self.bills.append(self.bill)
        return self.bills

    def calculate_fee_parking(self, data):
        try:
            if(self.check_files_exist(self.path, self.full_path) == False):
                raise Exception('Your car identity not found')
        except Exception:
            print("Your car identity not found")
            exit()
        else:
            self.get_bills_parking(data=data)
            total = sum([bill['sub_total'] for bill in self.bills])
            return [self.bills, total]

    def done_payment(self, total):
        self.get_available_credit()
        self.set_available_credit(-total)
        print("Payment success")
        print(f"Available Credits: {self.available_creadit}")
        self.save_customer_credit()