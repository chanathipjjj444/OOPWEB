class Room():
    def __init__(self, room_number, room_type, max_people, price_room, facilities_detail, bed_type, status):
        self.room_number = room_number
        self.room_type = room_type
        self.max_people = max_people
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
                updated_room = (self.room_number, self.room_type, self.max_people, self.price_room, self.facilities_detail, 
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
        new_room = (room_class.room_number, room_class.room_type, room_class.max_people, room_class.price_room, room_class.facilities_detail, 
                    room_class.bed_type, room_class.room_status)
        self.room_list.append(new_room)
        
room_cat = RoomCat()
room1 = Room(101, 'Standard', 3, 1000, 'TV, AC', 'Queen', True)
room2 = Room(102, 'Deluxe', 3, 2000, 'TV, AC, Jacuzzi', 'King', True)
room3 = Room(103, 'Deluxe', 4, 3000, 'TV, AC, Jacuzzi', 'Queen', True)
room_cat.add_room(room1)
room_cat.add_room(room2)
room_cat.add_room(room3)