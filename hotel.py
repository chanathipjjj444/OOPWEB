from fastapi import FastAPI
from typing import List
from pydantic import BaseModel
from datetime import datetime
from orderhistory import order_history

app = FastAPI()

class HotelCatalog:
    def __init__(self):
        self.hotel_list = []
    def add_hotel(self, hotel): #done
        self.hotel_list.append(hotel)

    def find_hotel(self, name): #done
        for hotel in self.hotel_list:
            if hotel.name_hotel == name:
                return hotel
            return ("Error: Hotel not found")

    def find_available_room(self, hotel_name,check_in, check_out,num_people):
        self.__available_rooms = []
        self.check_in = datetime.strptime(check_in, '%d-%m-%Y').date()
        self.check_out = datetime.strptime(check_out, '%d-%m-%Y').date()
        self.num_people = num_people
        hotel = self.find_hotel(hotel_name)
        if hotel:
            for room in hotel.get_room_list:
                available = True
                if self.num_people > room.get_max_people:
                    continue  # skip room if num_people > max_people
                for booking in order_history.history:
                    if  booking.hotel_name == hotel_name and booking.room_number == room.get_room_number:
                            # Check if the booking overlaps with the given dates
                            if self.check_out > booking.check_in and self.check_in < booking.check_out:
                                available = False 
                                
                if available == True:
                        if available == True and room.get_room_status == False:
                            room.get_room_status = True
                    # Check if the room is available for the given dates
                    
                        self.__available_rooms.append(room)
                        print("Room number:",room.get_room_number, "Type:",room.get_room_type, "Max_people:",room.get_max_people,
                              "Price:",room.get_price_room, "Facilities:",room.get_facilities_detail,"Room picture:",room.get_room_picture,
                              "Bed type:",room.get_bed_type, "Status:",room.get_room_status)
            if  len(self.__available_rooms) <= 0:
                print("No room available")
                return {"No room available"}
            return self.__available_rooms
        else:
            return None

    def find_add_on(self,hotel_name):
        hotel = self.find_hotel(hotel_name)
        if hotel:
            for add_on in hotel.get_add_on_hotel:
                print("Hotel name:",hotel_name,"Service type:",add_on.type_service, "Name:",add_on.name_service, "Detail:",add_on.detail,
                      "Picture:",add_on.picture ,"Price:",add_on.price_service)



    def show_hotel(self):
        for hotel in self.__hotel_list:
            print("Name hotel:",hotel.get_name_hotel, "Rating:",hotel.get_rating,"Num_rooms:",hotel.get_num_rooms,
                  "hotel_picture:",hotel.get_hotel_picture, "Location:",hotel.get_location, "Province:",hotel.get_province)

    def get_hotel_list(self):
        return self.__hotel_list

class Hotel:
    def __init__(self, name:str, rating:int, num_rooms:int, hotel_picture:str, location:str, province:str, hotel_room_list:list, add_on_hotel:str):
        self.name_hotel = name
        self.rating = rating
        self.num_rooms = num_rooms
        self.hotel_picture = hotel_picture
        self.location = location
        self.province = province
        self.room_list = hotel_room_list
        self.add_on_hotel = add_on_hotel


    ##################### เเก้เพิ่มหลังจากเห็นไฟล์ room.py ############################
    # def show_room(self):
    #     for room in self.room_list:
    #         return("Room number:",room.room_number, "type:",room.room_type,"max_people:",room.max_people,
    #               "price:",room.price_room, "facilities:",room.facilities_detail, "bed type:",room.bed_type, "status:",room.room_status)

class HotelToAdd(BaseModel):
    name_hotel: str
    rating: int
    num_rooms: int = 100
    hotel_picture: None | str = None
    location: str = "Thailand"
    province: str 
    room_list: List[str]
    add_on_hotel: None | str = None

