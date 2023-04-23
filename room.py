from hotel import Hotel,HotelCatalog
from pydantic import BaseModel
class Room():
    def __init__(self, room_number, room_type, max_people, price_room, facilities_detail, bed_type, room_picture,status):
        self.__room_number = room_number
        self.__room_type = room_type
        self.__max_people = max_people
        self.__price_room = price_room
        self.__facilities_detail = facilities_detail
        self.__bed_type = bed_type
        self.__room_picture = room_picture
        self.__room_status = status
    

    def update_status(self, hotel):
        self.__room_status = not self.__room_status
        for room in hotel.get_room_list:
            if room.__room_number == self.__room_number:
                room.__room_status = self.__room_status
                break

    def set_room_price(self, num_days):
        self.price = self.__price_room * num_days
        return self.price
    @property
    def get_room_number(self):
        return self.__room_number
    @property
    def get_room_type(self):
        return self.__room_type
    @property
    def get_max_people(self):
        return self.__max_people
    @property
    def get_price_room(self):
        return self.__price_room
    @property
    def get_facilities_detail(self):
        return self.__facilities_detail
    @property
    def get_bed_type(self):
        return self.__bed_type
    @property
    def get_room_picture(self):
        return self.__room_picture
    @property
    def get_room_status(self):
        return self.__room_status
