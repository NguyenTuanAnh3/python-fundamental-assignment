from models.bill import Bill
from handlers.dateHandler import DateHandler, DAY_OF_WEEK

class BillDateHandler(Bill):

    def __init__(self, start_day, leave_day):
        super().__init__()
        self.start_day = start_day
        self.end_day = leave_day
        self.date_handler = DateHandler()
        [self.day_time, self.night_time, self.new_day] = self.date_handler.separate_hour(self.start_day)
        
    def date_bill_handler(self, **kwargs):
        self.bill['date'] = self.date_handler.convert_date_to_string(self.start_day).split(" ")[0]
        self.bill['dayOfWeek'] = DAY_OF_WEEK[self.start_day.weekday()]
        if kwargs['start'] == '08:00' and kwargs['end'] == '16:59':
            self.day_time_handler(**kwargs)
        elif kwargs['start'] == '17:00' and kwargs['end'] == '23:59':
            self.night_time_handler(**kwargs)
        else:
            self.over_night_handler(**kwargs)

    def day_time_handler(self, **kwargs):
        temp_str = kwargs['start'] + ' - ' + kwargs['end']
        if (self.start_day < self.end_day and self.end_day < self.day_time):
            sub_time = round((self.end_day - self.start_day).seconds/3600)
            time_remain = sub_time - int(kwargs['maxStayInHours'])
        elif(self.day_time < self.start_day) :
            sub_time = 0
            time_remain = 0
        else:
            sub_time = round((self.day_time - self.start_day).seconds/3600)
            time_remain = sub_time - int(kwargs['maxStayInHours'])
        self.bill[temp_str] = [
            {
                "time": sub_time if sub_time <= 2 else kwargs['maxStayInHours'],
                "price_per_hour": sub_time if sub_time == 0 else kwargs['pricePerHour'],
                "str_price_per_hour": '' if sub_time == 0 else (f'${"{0:.2f}".format(kwargs["pricePerHour"])}/h') 
            },
            {
                "time": 0 if (sub_time == 0 or time_remain <= 0 ) else time_remain,
                "price_per_hour": 0 if time_remain <= 0 else kwargs['pricePerHour'] * 2,
                "str_price_per_hour": '' if time_remain <= 0 else (f'${"{0:.2f}".format(kwargs["pricePerHour"])}/h * 2') 
            }
        ]

    def night_time_handler(self, **kwargs):
        temp_str = kwargs['start'] + ' - ' + kwargs['end']
        if( self.day_time < self.start_day <= self.end_day and self.end_day < self.night_time):
            sub_time = round((self.end_day - self.start_day).seconds/3600)
        elif(self.day_time < self.start_day):
            sub_time = round((self.night_time - self.start_day).seconds/3600)
        elif(self.day_time < self.end_day < self.night_time):
            sub_time = round((self.end_day - self.day_time).seconds/3600) 
        elif(self.end_day < self.day_time):
            sub_time = 0     
        else:
            sub_time = round((self.night_time - self.day_time).seconds/3600)
            
        str_price_per_hour = f'${"{0:.2f}".format(kwargs["pricePerHour"])}/h' if sub_time != 0 else ''
        
        self.bill[temp_str] = [
            {
                "time": sub_time,
                "price_per_hour": kwargs['pricePerHour'] if sub_time != 0 else 0,
                "str_price_per_hour": str_price_per_hour
            }
        ]

    def over_night_handler(self, **kwargs):
        temp_str = kwargs['start'] + ' - ' + kwargs['end']
        sub_time = 1
        if(self.end_day < self.day_time or self.day_time < self.end_day < self.night_time):
            sub_time = 0
        elif(self.night_time < self.start_day < self.end_day):
            sub_time = round((self.end_day - self.start_day)/3600)

        str_price_per_hour = f'${"{0:.2f}".format(kwargs["pricePerHour"])}' if sub_time != 0 else ''

        self.bill[temp_str] = [
            {
                "time": 'N/A' if sub_time != 0 else 0,
                "price_per_hour": kwargs['pricePerHour'] if sub_time != 0 else 0,
                "str_price_per_hour": str_price_per_hour
            }
        ]
    