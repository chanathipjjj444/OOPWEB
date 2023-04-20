from hotel import HotelCatalog,Hotel,catalog
from history import OrderHistory
from datetime import datetime
from AddOns import add_on_cat
class Room():
    def __init__(self, room_number, room_type, max_people, price_room, facilities_detail, bed_type, status):
        self.room_number = room_number
        self.room_type = room_type
        self.max_people = max_people
        self.price_room = price_room
        self.facilities_detail = facilities_detail
        self.bed_type = bed_type
        self.room_status = status
    
    def update_status(self, hotel):
        self.room_status = not self.room_status
        for room in hotel.room_list:
            if room.room_number == self.room_number:
                room.room_status = self.room_status
                break
    def set_room_price(self, num_days):
        self.price = self.price_room * num_days
        return self.price

class Booking:
    def __init__(self, check_in, check_out, num_people, num_room):
        self.check_in = datetime.strptime(check_in, '%d-%m-%Y').date()
        self.check_out = datetime.strptime(check_out, '%d-%m-%Y').date()
        self.num_people = num_people
        self.num_room = num_room
        self.hotel_name = None
        self.room_number = None
        self.total_price = 0
        self.add_on_price = 0
    
    def get_num_days(self):
        self.totaldays = (self.check_out - self.check_in).days
        return {"total_day":self.totaldays}
    def set_total_price(self):
        self.total_price = self.room_price  + self.add_on_price
        return {"total_price":self.total_price}


    def book_room_check(self, hotel_name, room_number, catalog: HotelCatalog, order_history: OrderHistory):
        hotel = catalog.find_hotel(hotel_name)
        if hotel:
            
            for room in hotel.room_list:
               
                if room.room_number == room_number :
                    # Check if room is available for given dates
                    available = True
                    for booking in order_history.history:
                        if booking.hotel_name == hotel_name and booking.room_number == room_number:
                            # Check if the booking overlaps with the given dates
                            if self.check_out > booking.check_in and self.check_in < booking.check_out:
                                available = False 
                                break
                    if available == True:
                        # Book the room
                        if available == True and room.room_status == False:
                            room.room_status = True
                        
                        self.hotel_name = hotel_name
                        self.room_number = room_number
                        order_history.history.append(self)
                        room.update_status(hotel)
                        self.get_num_days()
                        
                        self.room_price =room.set_room_price(self.totaldays)
                        self.set_total_price()
                        
                        return {"message": "Booking successful","Room number": room_number, "Room Status": room.room_status,"Total days":self.totaldays,"Total price": self.total_price}
                    else:
                        return "Room not available for the given dates"
            else:
                return "Room not found"
        else:
            return "Hotel not found"


    def book_add_on(self, hotel_name, service_type, service_detail, catalog: HotelCatalog, requirement):
        hotel = catalog.find_hotel(hotel_name)
        if hotel:
            if requirement == False:
                return  {"No booking addon"}
            
            add_on_services = []
            for add_on in hotel.add_on_hotel:
                if add_on.type_service == service_type:
                    add_on_services.append(add_on)
                    
            if len(add_on_services) >0:
                
                for add_on in add_on_services:
                    if add_on.detail == service_detail:
                        if service_type == "breakfast":
                            self.price = add_on.price_food
                        elif service_type == "spa":
                            self.price = add_on.price_spa
                        else:
                            # Code for booking taxi service goes here
                            return "Taxi service not implemented yet"
                        self.add_on_price = add_on_cat.set_add_on_price(service_type,service_detail)
                        self.set_total_price()
                        return {"message": "service booked successfully", "service_type": service_type, "service_detail": service_detail, "price": self.price}
                    else:
                        return {"No this service_detail":service_detail,"found in hotel":hotel_name}
            else:
                return {"No this service_type":service_type,"found in hotel":hotel_name}
        else:
            print("Unable to find hotel")
