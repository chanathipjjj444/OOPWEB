class Hotel:
    def __init__(self, name, num_rooms, room_list):
        self.name = name
        self.num_rooms = num_rooms
        self.room_list = room_list

class HotelCatalog:
    def __init__(self):
        self.hotel_list = []

    def add_hotel(self, hotel):
        self.hotel_list.append(hotel)

    def find_hotel(self, name):
        for hotel in self.hotel_list:
            if hotel.name == name:
                return hotel
        print("Error: Hotel not found")
        return None
    
# Import the class that contains the attribute
#from other_module import OtherClass
class Room():
    def __init__(self, room_number, room_type, price_room, facilities_detail, bed_type, status):
        self._room_number = room_number
        self._room_type = room_type
        self._price_room = price_room
        self._facilities_detail = facilities_detail
        self._bed_type = bed_type
        self._room_status = status
    '''
    def update_status(self, hotel):
        self._room_status = not self._room_status
        for room in hotel.room_list:
            if room._room_number == self._room_number:
                room._room_status = self._room_status
                break
    '''
    def update_status(self, hotel):
        self._room_status = not self._room_status
        for room in hotel.room_list:
            if room._room_number == self._room_number:
                room._room_status = self._room_status
                break
        '''
        for room in room_cat.room_list:
            if room[0] == self._room_number:
                room_cat.room_list.remove(room)
                updated_room = (self._room_number, self._room_type, self._price_room, self._facilities_detail, 
                                self._bed_type, self._room_status)
                room_cat.room_list.append(updated_room)
                break
        '''
        for i, room in enumerate(room_cat.room_list):
            if room[0] == self._room_number:
                updated_room = (self._room_number, self._room_type, self._price_room, self._facilities_detail, 
                                self._bed_type, self._room_status)
                room_cat.room_list[i] = updated_room
                break
        
# Define the class to add the new list to
class RoomCat:
    def __init__(self):
        self.room_list = []

    def add_room(self, room_class):
        new_room = (room_class._room_number, room_class._room_type, room_class._price_room, room_class._facilities_detail, 
                    room_class._bed_type, room_class._room_status)
        self.room_list.append(new_room)

class Booking:
    def __init__(self, room_catalog):
        self.room_catalog = room_catalog

    def get_room_list(self):
        return self.room_catalog.room_list
    
    def book_room_in_hotel(self, hotel_name, room_number):
        hotel = catalog.find_hotel(hotel_name)
        if hotel:
            for room in hotel.room_list:
                if room._room_number == room_number: #check เลขห้อง
                    if room._room_status == True:
                        room.update_status(hotel) #update_status
                        print("Room booked successfully!")
                        print("Room status:",room_number,":",room._room_status) #show status
                        return True
                    else:
                        print("Unable to book room.")
                        return False
            print("Unable to find room")
        else:
            print("Unable to find hotel.")

room_cat = RoomCat()
room1 = Room(101, 'Standard', 1000, 'TV, AC', 'Queen', True)
room2 = Room(102, 'Deluxe', 2000, 'TV, AC, Jacuzzi', 'King', True)
room_cat.add_room(room1)
room_cat.add_room(room2)
print(room_cat.room_list)

booking = Booking(room_cat)

# create a hotel with some rooms
hotel1 = Hotel('Hotel A', 2, [room1, room2])

# create a hotel catalog and add the hotel
catalog = HotelCatalog()
catalog.add_hotel(hotel1)

print("Before booking:")
#print("hotel1 room status:", hotel1.room_list[0]._room_status)
#print("room_cat room status:", room_cat.room_list[0][-1])

booking.book_room_in_hotel('Hotel A', 101)

print("After booking:")
#print("hotel1 room status:", hotel1.room_list[0]._room_status)
#print("room_cat room status:", room_cat.room_list[0][-1])

print(room_cat.room_list)

booking.book_room_in_hotel("Hotel A", 101)