import datetime

DAY_OF_WEEK = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

class DateHandler:
    
    def convert_date_type(self, str_date):
        return datetime.datetime.strptime(str_date, "%Y-%m-%d %H:%M")

    def convert_date_to_string(self, date):
        return date.strftime("%Y-%m-%d %H:%M")

    def get_date_range(self, start, end):
        return [(start + datetime.timedelta(days=delta)).strftime('%Y-%m-%d') for delta in range((end - start).days + 1)]

    def separate_hour(self, day):
        day_time = day.replace(hour=16, minute=59)
        night_time = day.replace(hour=23, minute=59)
        new_day = (day + datetime.timedelta(days=1)).replace(hour=8, minute=0)
        return [day_time, night_time, new_day] 

        