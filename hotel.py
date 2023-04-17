from fastapi import FastAPI
from typing import List
from pydantic import BaseModel

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

    def show_add_on(self, HotelName):
        for hotel in self.hotel_list:
            if hotel.name_hotel == HotelName:
                return hotel.add_on_hotel
        return ("Error: Hotel not found")

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

