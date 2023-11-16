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
    
    def __init__(self, car_identity, leave_day):
        super().__init__(car_identity)
        self.leave_day = leave_day
        self.info = {}
        self.bill = {}

    def get_arrival_day(self):
        get_arrival_time =  self.get_customer_information()[ARRIVAL_TIME_TEXT].strip()
        return datetime.datetime.strptime(get_arrival_time, "%Y-%m-%d %H:%M")

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

    def get_fee_each_day(self, start_day, data):
        [day_time, night_time, new_day] = self.split_periods_day(start_day)
        self.bill['date'] = start_day.strftime("%Y-%m-%d")
        self.bill['dayOfWeek'] = DAY_OF_WEEK[start_day.weekday()]
        parking_regulation = data[self.bill['dayOfWeek']]
        for park in parking_regulation:
            temp_str = park['start'] + ' - ' + park['end']
            
            if park['start'] == '08:00' and park['end'] == '16:59':
               sub_time = round((day_time - start_day).seconds/3600)
               self.bill[temp_str] = [
                {
                    "time": park['maxStayInHours'],
                    "price_per_hour": park['pricePerHour']
                },
                {
                    "time": sub_time - int(park['maxStayInHours']),
                    "price_per_hour": park['pricePerHour'] * 2
                }
               ]
            elif park['start'] == '17:00' and park['end'] == '23:59':
                sub_time = (night_time - day_time).seconds//3600
                self.bill[temp_str] = [
                {
                    "time": sub_time,
                    "price_per_hour": park['pricePerHour']
                }
               ]
            else:
                self.bill[temp_str] = [
                {
                    "time": 'N/A',
                    "price_per_hour": park['pricePerHour']
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

    def calculate_fee_parking(self, data):
        try:
            if(self.is_customer_information_exist() == False):
                raise Exception('Your car identity not found')
        except Exception:
            print("Your car identity not found")
        else:
            self.get_fee_each_day(self.get_arrival_day(), data)
            print(self.calculate_sub_total_each_day())
            return 