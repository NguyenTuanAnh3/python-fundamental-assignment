import json
from classes.park import Park
from datetime import datetime
from options import park_option, pickup_option, history_option


your_option = input("Choose your option? (park, pickup, history): ")

if(your_option == 'park'):
    park_option()
elif (your_option == 'pickup'):
    with open('parkingAreaPrice.json') as f:
        data = json.load(f)
    pickup_option(data)
elif (your_option == 'history'):
    history_option()