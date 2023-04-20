class Hotel:
    def __init__(self, name_hotel, rating, num_rooms, hotel_picture, location, province):
        self.name_hotel = name_hotel
        self.rating = rating
        self.num_rooms = num_rooms
        self.hotel_picture = hotel_picture
        self.location = location
        self.province = province
        self.room_list = []
        self.add_on_hotel = []

    def show_room(self):
        for room in self.room_list:
            print("Room number:",room.room_number, "type:",room.room_type,"max_people:",room.max_people,
                  "price:",room.price_room, "facilities:",room.facilities_detail, "bed type:",room.bed_type, "status:",room.room_status)
    def show_add_on(self):
        for add_on in self.add_on_hotel:
            print("Addon in this Hotel:",add_on.add_on_list)  

    def show_hotel(self,hotel_catalog:object):
        self.hotel_catalog = hotel_catalog
        for hotel in self.hotel_catalog.hotel_list:
            print("Name hotel:",hotel.name_hotel, "Rating:",hotel.rating,"Num_rooms:",hotel.num_rooms,
                  "hotel_picture:",hotel.hotel_picture, "Location:",hotel.location, "Province:",hotel.province)
            
    #add function add room
    def add_room(self, room):
        self.room_list.append(room)
        return {"message": "Room added successfully", "room_list": self.room_list}
    #add function add add on
    def add_addons(self,add_on):
        self.add_on_hotel.append(add_on)
        return {"message": "Addon added successfully", "add_on_hotel": self.add_on_hotel}
    
    
    
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
    
    def find_available_room(self, name):
        self.available_rooms = []
        hotel =self.find_hotel(name)

        if hotel:
            for room in hotel.room_list:
                if room.room_status == True:
                    self.available_rooms.append(room)
                    return  self.available_rooms
                else:
                    return {"No room available"}
        
    def find_add_on(self, name):

        hotel =self.find_hotel(name)

        if hotel:
            for add_on in hotel.add_on_hotel:
                print(add_on) 
        else:
            return None
    
    
catalog = HotelCatalog()
