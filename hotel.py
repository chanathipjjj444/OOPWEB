from fastapi import FastAPI
from typing import List
from pydantic import BaseModel

class Room(BaseModel):
    room_type: str
    num_rooms: int

class Hotel(BaseModel):
    name_hotel: str
    room_list: List[Room]


app = FastAPI()


class Hotel:
    def __init__(self, name, rating, num_rooms, hotel_picture, location, province, hotel_room_list, add_on_hotel):
        self.name_hotel = name
        self.rating = rating
        self.num_rooms = num_rooms
        self.hotel_picture = hotel_picture
        self.location = location
        self.province = province
        self.room_list = hotel_room_list
        self.add_on_hotel = add_on_hotel

    def show_room(self):
        for room in self.room_list:
            print("Room number:",room.room_number, "type:",room.room_type,"max_people:",room.max_people,
                  "price:",room.price_room, "facilities:",room.facilities_detail, "bed type:",room.bed_type, "status:",room.room_status)
    
    def show_add_on(self):
        for add_on in self.add_on_hotel:
            print("Addon in this Hotel:",add_on.add_on_list)

class HotelCatalog:
    def __init__(self):
        self.hotel_list = []

    def add_hotel(self, hotel:Hotel):
        self.hotel_list.append(hotel)

    def find_hotel(self, name):
        for hotel in self.hotel_list:
            if hotel.name_hotel == name:
                pass
                # return hotel
        print("Error: Hotel not found")
        # return None



hotel1 = Hotel("Hotel A", 4, 100, "picture", "Thailand", "Chonburi", ["a","b","c"], "add_on_hotel")
# hotel2 = Hotel("Hotel B", 5, 200, "picture", "Thailand", "Chonburi", ["a","b","c"], "add_on_hotel")

catalog = HotelCatalog()

    # @app.get("/hotels")
    # def show_hotel():
    #     return catalog.hotel_list

    # @app.get("/hotels/{name}")
    # def show_hotel1(name: str):
    #     return catalog.find_hotel(name)

@app.post("/hotels")
async def add_hotel(hotel):
    catalog.add_hotel(hotel)
    return {"message": "Hotel added successfully"}

add_hotel(hotel1)



# @app.post("/hotels")
# def add_hotel(hotel: Hotel):
#     catalog.add_hotel(hotel)
#     return {"message": "Hotel added successfully"}

# @app.post("/hotels")
# async def add_hotel(hotel: Hotel):
#     catalog.add_hotel(hotel)
#     return "{hotel.name_hotel} added"

# @app.get("/findhotel/{name}")
# async def show_room(catalog: HotelCatalog, name: str):
#     catalog.find_hotel(name)
#     return catalog.find_hotel(name)

# add_hotel(hotel1)
