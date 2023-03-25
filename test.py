#everything in this is public
class Hotel:
    def __init__(self, name, rating, num_rooms, hotel_picture, location, province, room_list, add_on_hotel):
        self.name_hotel = name
        self.rating = rating
        self.num_rooms = num_rooms
        self.hotel_picture = hotel_picture
        self.location = location
        self.province = province
        self.room_list = room_list
        self.add_on_hotel = add_on_hotel

    def show_room(self):
        for room in self.room_list:
            print("Room number:",room.room_number, "type:",room.room_type, 
                  "price:",room.price_room, "facilities:",room.facilities_detail, "bed type:",room.bed_type, "status:",room.room_status)
    def show_add_on(self):
        for add_on in self.add_on_hotel:
            print("Addon :",add_on.add_on_list)            
    '''
    def show_add_on(self, addon_object):
        for add_on in addon_object.add_on_list:
            print("Addon in hotel:",addon_object.add_on_list)
    '''
    
class HotelCatalog:
    def __init__(self):
        self.hotel_list = []
        

    def add_hotel(self, hotel):
        self.hotel_list.append(hotel)

    def find_hotel(self, name):
        for hotel in self.hotel_list:
            if hotel.name_hotel == name:
                return hotel
        print("Error: Hotel not found")
        return None
    
    
class Room():
    def __init__(self, room_number, room_type, price_room, facilities_detail, bed_type, status):
        self.room_number = room_number
        self.room_type = room_type
        self.price_room = price_room
        self.facilities_detail = facilities_detail
        self.bed_type = bed_type
        self.room_status = status
    '''
    def update_status(self, hotel):
        self._room_status = not self._room_status
        for room in hotel.room_list:
            if room._room_number == self._room_number:
                room._room_status = self._room_status
                break
    '''
    def update_status(self, hotel):
        self.room_status = not self.room_status
        for room in hotel.room_list:
            if room.room_number == self.room_number:
                room.room_status = self.room_status
                break
        for i, room in enumerate(room_cat.room_list):
            if room[0] == self.room_number:
                updated_room = (self.room_number, self.room_type, self.price_room, self.facilities_detail, 
                                self.bed_type, self.room_status)
                room_cat.room_list[i] = updated_room
                break
    '''
    def update_status(self, hotel):
        self.room_status = not self.room_status
        for room in hotel.room_list():
            if room.room_number() == self.room_number:
                for i, room in enumerate(room_cat.room_list):
                    if room[0] == self.room_number: #check room_number
                        updated_room = (self.room_number, self.room_type, self.price_room, self.facilities_detail, 
                                self.bed_type, self.room_status)
                        room_cat.room_list[i] = updated_room
        room.room_status() == self.room_status
    '''
                
# Define the class to add the new list to
class RoomCat:
    def __init__(self):
        self.room_list = []

    def add_room(self, room_class):
        new_room = (room_class.room_number, room_class.room_type, room_class.price_room, room_class.facilities_detail, 
                    room_class.bed_type, room_class.room_status)
        self.room_list.append(new_room)


class Addons:
    def __init__(self):
        self.add_on_list  =[]
    '''    
    def get_addons(self, detail, all_services):
        addons = (all_services.__type_food)
        self.__detail = detail
        self.__add_on_list.append(addons)
    '''
    def add_breakfast_service(self, breakfast):
        breakfast_list=(breakfast.detail ,breakfast.type_food, breakfast.price_food)
        self.add_on_list.append(breakfast_list)
    
    def get_add_on_list(self):
        return self.add_on_list

class BreakfastService():
    def __init__(self, detail, type_food, price_food):
        self.detail = detail
        self.type_food = type_food
        self.price_food = price_food
    '''
    def get_detail(self):
        return self.detail
    def get_type_food(self):
        return self.type_food
    def get_price_food(self):
        return self.price_food
    '''

class SpaService:
    def __init__(self, detail,reserve_spa, price_service):
        self.detail = detail
        self.reserve_spa = reserve_spa
        self.price_service = price_service

class ActivityService:
    def __init__(self, detail, date_activity, price_activity, num_person):
        self.detail = detail
        self.data_activity = date_activity
        self.price_activity = price_activity
        self.num_person = num_person

class TaxiService:
    def __init__(self, detail,number_taxi, fees_taxi, contact_taxi):
        self.detail = detail
        self.number_taxi = number_taxi
        self.fees_taxi = fees_taxi
        self.contact_taxi = contact_taxi

class Booking:
    def __init__(self, room_catalog):
        self.room_catalog = room_catalog

    def get_room_list(self):
        return self.room_catalog.room_list
    
    def book_room_in_hotel(self, hotel_name, room_number):
        hotel = catalog.find_hotel(hotel_name)
        if hotel:
            for room in hotel.room_list:
                if room.room_number == room_number: #check เลขห้อง
                    if room.room_status == True:
                        room.update_status(hotel) #update_status
                        print("Room booked successfully!")
                        print("Room status:",room_number,":",room.room_status) #show status
                        return True
                    else:
                        print("Unable to book room.")
                        return False
            print("Unable to find room")
        else:
            print("Unable to find hotel.")
            
    '''
    def booking_add_on(self, hotel_name, requirement): #input hotel_name and requirement
        hotel = catalog.find_hotel(hotel_name)
        if hotel:
            for add_on in hotel.add_on_hotel: #check add_on in hotel
                if requirement == True:
    '''


room_cat = RoomCat()
room1 = Room(101, 'Standard', 1000, 'TV, AC', 'Queen', True)
room2 = Room(102, 'Deluxe', 2000, 'TV, AC, Jacuzzi', 'King', True)
room3 = Room(103, 'Deluxe', 3000, 'TV, AC, Jacuzzi', 'Queen', True)
room_cat.add_room(room1)
room_cat.add_room(room2)
room_cat.add_room(room3)

add_on_cat = Addons()
breakfast1 = BreakfastService("breakfast","soup", 100)
breakfast2 = BreakfastService("breakfast","beverage",50)
add_on_cat.add_breakfast_service(breakfast1)
add_on_cat.add_breakfast_service(breakfast2)

add_on_cat2 = Addons()
breakfast3 = BreakfastService("breakfast","salad", 100)
breakfast4 = BreakfastService("breakfast","buffe",50)
add_on_cat2.add_breakfast_service(breakfast3)
add_on_cat2.add_breakfast_service(breakfast4)

hotel1 = Hotel('Hotel A', 5, 2, "A", "Lardprao", "Bangkok", [room1, room2],[add_on_cat])

# create a hotel catalog and add the hotel
catalog = HotelCatalog()
catalog.add_hotel(hotel1)
print("before booking")
hotel1.show_add_on()
hotel1.show_room()

book1=Booking(room_cat)
book1.book_room_in_hotel("Hotel A", 101)

hotel1.show_room()
