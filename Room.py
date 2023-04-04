class Room():
    def __init__(self):
        self.__room_type = []
        self.__price_room = []
        self.__facilities_detail = []
        self.__bed_type = []
        self.__room_picture = []
        self.__room_number = []
        self.__room_status = []
    def select_filters_room(self):
        pass
    def select_addons(self):
        pass
    def create_booking_room(self):
        pass
    def create_room(self):
        pass

class Addons:
    def __init__(self):
        self.__detail = []
        self.__add_on_list  =[]
    def get_addons(self):
        pass

class BreakfastService():
    def __init__(self):
        self.__type_food = []
        self.__price_food = []

class SpaService:
    def __init__(self):
        self.__reserve_spa = []
        self.__price_service = []

class ActivityService:
    def __init__(self):
        self.__data_activity = []
        self.__price_activity = []
        self.__num_person = []

class TaxiService:
    def __init__(self):
        self.__number_taxi = []
        self.__fees_taxi = []
        self.__contact_taxi = []