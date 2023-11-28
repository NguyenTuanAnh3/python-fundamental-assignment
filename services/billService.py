import datetime
from models.bill import Bill
from services.customerService import CustomerService
from handlers.dateHandler import DateHandler, DAY_OF_WEEK
from handlers.fileHandler import FileHandler
from handlers.billDateHandler import BillDateHandler

class BillService(Bill):
    
    def __init__(self, car_identity, leave_day):
        super().__init__()
        self.customer_service = CustomerService(car_identity=car_identity)
        self.date_handler = DateHandler()
        self.file_handler = FileHandler()
        
        self.arrival_time = self.customer_service.get_arrival_time()
        self.leave_time = self.date_handler.convert_date_type(leave_day)
        self.fixed_price_data = self.file_handler.get_information_json()
     
    def get_fee_information_per_day(self, start_day, leave_day):
        bill_date_handler = BillDateHandler(start_day=start_day, leave_day=leave_day)
        parking_regulation = self.fixed_price_data[DAY_OF_WEEK[start_day.weekday()]]
        
        for park in parking_regulation:
            bill_date_handler.date_bill_handler(**park)

        self.bill = bill_date_handler.bill
        return self.bill 

    def get_sub_total_per_day(self):
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

    def get_bills_information_parking(self):
        start_day = self.arrival_time
        end_day = self.leave_time
        range_date = self.date_handler.get_date_range(start=start_day, end=end_day)
        for index, day in enumerate(range_date):
            day = datetime.datetime.strptime(day, "%Y-%m-%d")
            next_day = (day + datetime.timedelta(days=1)).replace(hour=8, minute=0)
            self.bill = {}
            if index == 0 and len(range_date) > 1:
                self.get_fee_information_per_day(start_day=start_day, leave_day= next_day)
                self.get_sub_total_per_day()
            elif index == 0 and len(range_date) == 1:
                self.get_fee_information_per_day(start_day=start_day, leave_day= end_day)
                self.get_sub_total_per_day()
                self.bills.append(self.bill)
                return self.bills
            elif (index == len(range_date) - 1) :
                previous_time = end_day.replace(hour=8, minute=0)
                self.get_fee_information_per_day(start_day=previous_time, leave_day= end_day)
                self.get_sub_total_per_day()
            else:
                day = day.replace(hour=8, minute=0)
                self.get_fee_information_per_day(start_day=day, leave_day= next_day)
                self.get_sub_total_per_day()
            self.bills.append(self.bill)
        return self.bills

    def get_bills_and_total_fee_parking(self):
        self.get_bills_information_parking()
        total = sum([bill['sub_total'] for bill in self.bills])
        return [self.bills, total]




        

    