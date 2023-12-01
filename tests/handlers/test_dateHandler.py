from handlers.dateHandler import DateHandler
import datetime

class TestDateHandler:

    @classmethod
    def setup_class(self):
        self.date_handler = DateHandler()

    def test_convert_date_type(self):
        date_test = '2023-11-30 00:00'
        assert self.date_handler.convert_date_type('2023-11-30 00:00').strftime("%Y-%m-%d %H:%M") == date_test

    def test_convert_date_to_string(self):
        date = datetime.datetime.now().replace(hour=0, minute=0)
        assert self.date_handler.convert_date_to_string(date=date) ==  "2023-11-30 00:00"

    def test_get_date_range(self):
        start_day = datetime.datetime.strptime("2023-11-28", "%Y-%m-%d")
        end_day =  datetime.datetime.strptime("2023-11-30", "%Y-%m-%d")

        assert self.date_handler.get_date_range(start=start_day, end=end_day) == ['2023-11-28', '2023-11-29', '2023-11-30']

    def test_separate_hour(self):
        today = datetime.datetime.now()
        day_time = today.replace(hour=16, minute=59)
        night_time = today.replace(hour=23, minute=59)
        new_day = (today + datetime.timedelta(days=1)).replace(hour=8, minute=0)
        assert self.date_handler.separate_hour(day=today) == [day_time, night_time, new_day] 