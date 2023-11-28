from services.parkService import ParkService
from services.pickUpService import PickUpService
from services.historyService import HistoryService

your_option = input("Choose your option? (park, pickup, history): ")
if(your_option == 'park'):
    try:
        park_service = ParkService()
        park_service.handle_park()
    except Exception as ex:
        print(ex)
elif (your_option == 'pickup'):
    try:
        pickup_service = PickUpService()
        pickup_service.handle_pickup()
    except Exception as ex:
        print(ex)
elif (your_option == 'history'):
    try:
        enter_car_identity = input("Please enter your car identity: ") 
        history_service = HistoryService(car_identity=enter_car_identity)
        history_service.get_history_customer()
    except FileNotFoundError:
        print('Car identity not found')
    except Exception as ex:
        print(ex)