class Room():
    def __init__(self, room_type, price_room, facilities_detail, bed_type, room_picture, room_number, room_status):
        self.__room_type = room_type
        self.__price_room = price_room
        self.__facilities_detail = facilities_detail
        self.__bed_type = bed_type
        self.__room_picture = room_picture
        self.__room_number = room_number
        self.__room_status = room_status
    def select_filters_room(self):
        pass
    def select_addons(self):
        pass
    def create_booking_room(self):
        pass
    def create_room(self):
        pass

class Addons:
    def __init__(self, detail):
        self.__detail = detail
        self.__add_on_list  =[]
    def get_addons(self):
        pass

class BreakfastService():
    def __init__(self, type_food, price_food):
        self.__type_food = type_food
        self.__price_food = price_food

class SpaService:
    def __init__(self, reserve_spa, price_service):
        self.__reserve_spa = reserve_spa
        self.__price_service = price_service

class ActivityService:
    def __init__(self, date_activity, price_activity, num_person):
        self.__data_activity = date_activity
        self.__price_activity = price_activity
        self.__num_person = num_person

class TaxiService:
    def __init__(self, number_taxi, fees_taxi, contact_taxi):
        self.__number_taxi = number_taxi
        self.__fees_taxi = fees_taxi
        self.__contact_taxi = contact_taxi