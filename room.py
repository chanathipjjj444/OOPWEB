from hotel import HotelCatalog
from datetime import datetime
from orderhistory import OrderHistory
from pydantic import BaseModel
from addons import add_on_cat

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

class Booking:
    def __init__(self, check_in, check_out, num_people, num_room):
        self.check_in = datetime.strptime(check_in, '%d-%m-%Y').date()
        self.check_out = datetime.strptime(check_out, '%d-%m-%Y').date()
        self.num_people = num_people
        self.num_room = num_room
        self.hotel_name = None
        self.room_number = None
        self.room_price = 0
        self.add_on_price = 0
        self.total_price = 0
        self.total_days = 0
          
    def get_num_days(self):
        self.total_days = (self.check_out - self.check_in).days
        return {"total_day":self.total_days}

    def set_total_price(self):
        self.total_price = self.room_price  + self.add_on_price
        return {"total_price":self.total_price}

    def book_room_check(self, hotel_name, room_number, catalog: HotelCatalog, order_history: OrderHistory):
        hotel = catalog.find_hotel(hotel_name)
        if hotel:
            
            for room in hotel.get_room_list:
               
                if room.get_room_number == room_number :
                    # Check if room is available for given dates
                                            
                        self.hotel_name = hotel_name
                        self.room_number = room_number
                        order_history.history.append(self)
                        room.update_status(hotel)
                        self.get_num_days()
                        #self.set_room_price(room)
                        self.room_price =room.set_room_price(self.total_days)
                        self.set_total_price()

                        return {"message": "Booking successful","Room number": room_number, "Room Status": room.get_room_status}
                    
            else:
                return "Room not found"
        else:
            return "Hotel not found"

    def book_add_on(self, service_type, name_service, catalog: HotelCatalog, requirement):
        hotel = catalog.find_hotel(self.hotel_name)
        if hotel:
            if requirement == False:
                return  {"No booking addon"}    
            add_on_services = []
            for add_on in hotel.get_add_on_hotel:
                if add_on.type_service == service_type:
                    add_on_services.append(add_on)
                    
            if len(add_on_services) >0:
                
                for add_on in add_on_services:
                    if add_on.name_service == name_service:
                        
                        self.add_on_price = add_on_cat.set_add_on_price(service_type,name_service)
                        self.set_total_price()
                        return {"message": "service booked successfully", "service_type": service_type, "service_detail": name_service, "price": self.add_on_price}
                    else:
                        return {"No this service_detail":name_service,"found in hotel":self.hotel_name}
            else:
                return {"No this service_type":service_type,"found in hotel":self.hotel_name}
        else:
            print("Unable to find hotel")