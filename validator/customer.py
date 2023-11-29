class CustomerValidator:
    
    def check_car_identity_valid(self, car_identity):
        separate = car_identity.split("-")
        if separate[0][0:2].isnumeric() and separate[0][2].isupper() and len(separate[1]) == 5 and separate[1].isnumeric():
            return car_identity
        raise Exception("Invalid car identity")


    def  check_frequent_parking_number_valid(self, frequent_parking_number):
        if (frequent_parking_number == "" or frequent_parking_number == None) or (len(str(frequent_parking_number)) == 5 and frequent_parking_number.isnumeric()):
            if(frequent_parking_number == "" or frequent_parking_number == None):
                return None
            return frequent_parking_number
        raise Exception("Invalid frequent parking identity")