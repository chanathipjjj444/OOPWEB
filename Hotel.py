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
            print("Room number:",room.room_number, "type:",room.room_type,"max_people:",room.max_people,
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