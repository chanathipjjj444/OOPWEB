from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

from AddOns import Addons,BreakfastService,SpaService,TaxiService,ActivityService
from room import Room,RoomList,Booking
from hotel import Hotel,HotelCatalog,catalog

app = FastAPI()

class BreakfastServiceRequest(BaseModel):
    type_service: str
    detail: str
    type_food: str
    price_food: int

class SpaServiceRequest(BaseModel):
    type_service: str
    detail: str
    spa_picture: str
    price_spa: int


addons = Addons()
'''
@app.post("/breakfast")
async def add_breakfast_service(breakfast: BreakfastServiceRequest):

        #breakfast_service = BreakfastService(type_service=breakfast.type_service,detail=breakfast.detail,type_food=breakfast.type_food,price_food=breakfast.price_food)
        addons.add_breakfast_service(breakfast)
        return {"message": "Breakfast service added successfully"}
 
@app.post("/spa")
async def add_spa_service(spa: SpaServiceRequest):
        #spa_service = SpaService(type_service=spa.type_service,detail=spa.detail,spa_picture=spa.spa_picture,price_spa=spa.price_spa)
        addons.add_spa_service(spa)
        return {"message": "Spa service added successfully"}
'''    

@app.get("/addons")
async def get_add_on_list():
    return {"add_on_list": addons.get_add_on_list()}

class RoomToAdd(BaseModel):
    room_number: int
    room_type: str
    max_people: int
    price_room: float
    facilities_detail: str
    bed_type: str
    room_status: bool


class HotelToAdd(BaseModel):
    name_hotel: str
    rating: int
    num_rooms: int = 100
    hotel_picture: None | str = None
    location: str = "Thailand"
    province: str 
    room_list = []
    add_on_hotel = []

@app.post("/hotels")
async def add_hotel(hotel: HotelToAdd):

    catalog.add_hotel(hotel)
    return catalog.hotel_list


@app.post("/hotels_room")
async def add_hotel_room(hotel_name:str , room: RoomToAdd):
    # Access the room_list attribute and loop through the rooms
    hotel = catalog.find_hotel(hotel_name)

    if hotel is None:
        return {"error": f"Hotel '{hotel_name}' not found"}

    # Add the room to the hotel's room_list
    hotel.room_list.append(room)

    return catalog.hotel_list

@app.post("/hotels_addon")                              #รู้สึกว่าน่าจะมีวิธีอื่นที่ง่ายกว่านี้
async def add_addon_hotel(hotel_name: str, breakfast: BreakfastServiceRequest,spa: SpaServiceRequest):
    # Get the hotel object from the catalog
    hotel = catalog.find_hotel(hotel_name)

    if hotel is None:
        return {"error": f"Hotel '{hotel_name}' not found"}

    # Add the add-on service to the hotel's add_on_hotel list
    hotel.add_on_hotel.append(breakfast)
    hotel.add_on_hotel.append(spa)

    return catalog.hotel_list




@app.get("/hotels/{name}/rooms")
def show_add_on(name: str):
    return catalog.show_add_on(name)
