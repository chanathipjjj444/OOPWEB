from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

from AddOns import Addons,BreakfastService,SpaService,TaxiService,ActivityService
from room import Room,RoomList,Booking
from hotel import Hotel,HotelCatalog,catalog

app = FastAPI()

room1 = Room(101, 'Standard', 3, 1000, 'TV, AC', 'Queen', True)
room2 = Room(102, 'Deluxe', 3, 2000, 'TV, AC, Jacuzzi', 'King', True)
add_on_cat = Addons()
breakfast1 = BreakfastService("breakfast","corn soup","soup", 100)
breakfast2 = BreakfastService("breakfast","sisler salad","salad",120)
spa1 = SpaService("spa","Open 9am","picture",100)
add_on_cat.add_breakfast_service(breakfast1)
add_on_cat.add_spa_service(spa1)
add_on_cat.add_breakfast_service(breakfast2)

hotel1 = Hotel('Hotel A', 5, 2, "A", "Lardprao", "Bangkok", [room1],[add_on_cat])
#hotel1.add_room(room1)
#hotel1.add_room(room2)
catalog = HotelCatalog()
catalog.add_hotel(hotel1)

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

    def update_status(self, hotel):
        self.room_status = not self.room_status
        for room in hotel.room_list:
            if room.room_number == self.room_number:
                room.room_status = self.room_status
                break


class HotelToAdd(BaseModel):
    name_hotel: str
    rating: int
    num_rooms: int = 100
    hotel_picture: None | str = None
    location: str = "Thailand"
    province: str 
    room_list = []
    add_on_hotel = []
    
    # add function add room
    def add_room(self, room):
        self.room_list.append(room)



@app.post("/hotels")
async def add_hotel(hotel: HotelToAdd):
    
    hotel_obj = Hotel(hotel.name_hotel, hotel.rating, hotel.num_rooms, hotel.hotel_picture,hotel.location, hotel.province, [], [])
    catalog.add_hotel(hotel_obj)
    return hotel_obj



@app.post("/hotels_room")
async def add_hotel_room(hotel_name:str , room: RoomToAdd):
    # Access the room_list attribute and loop through the rooms
    hotel = catalog.find_hotel(hotel_name)

    if hotel is None:
        return {"error": f"Hotel '{hotel_name}' not found"}
    


    # Add the room to the hotel's room_list
    hotel.add_room(room)

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

@app.get("/hotellist")
async def get_hotel_list():
    return {"hotel_list": catalog.hotel_list}

@app.get("/show_available_room")
async def find_available_room(hotel_name:str):
        
    catalog.find_available_room(hotel_name)

    return {"hotel_name":hotel_name,"available_room":catalog.available_rooms}

@app.post("/book_room")
def book_room(check_in : str,check_out:str,num_people:int,num_room:int, hotel_name: str, room_number: int):
    # Create an instance of Booking class
    global booking
    booking=Booking(check_in = check_in,check_out= check_out,num_people= num_people,num_room=num_room)
    
    result = booking.book_room_check(hotel_name = hotel_name, room_number = room_number,catalog = catalog)
    # Return the result as JSON
    return {"result": result,"check in reserve": booking.date_check_in_reserve, "checkout reserve": booking.date_check_out_reserve}



@app.post("/book_add_on")                                                                          #ยังไม่เสร็จดี
def book_room(hotel_name:str,requirement : str, type_service : str, choice : int ):
    # Create an instance of Booking class

    
    booking.booking_add_on(hotel_name = hotel_name , requirement= requirement, type_input= type_service ,choice= choice, catalog = catalog)
    # Return the result as JSON
    return booking.result




@app.get("/hotels/{name}/rooms")
def show_add_on(name: str):
    return catalog.show_add_on(name)



book1=Booking("13-3-2021","15-3-2021",3,1)

book1.booking_add_on("Hotel A","True","breakafast",1,catalog)

#เหลือตรง add_on
