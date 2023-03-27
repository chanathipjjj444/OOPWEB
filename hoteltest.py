# list_hotel = ["hotel"]
# date_check_in_reserve =["3-21-2023"]
# date_check_out_reserve = ["3-25-2023"]
# room_avalible =[]
from data import *

class Booking:
    def __init__(self,name_hotel,check_in,check_out,num_room,num_people):
        self.name_hotel = name_hotel
        # self.room_type = room_type
        # self.bed_type = bed_type
        # self.price = price
        self.check_in = check_in
        self.check_out = check_out
        self.num_room = num_room
        self.num_people = num_people
        self.list_hotel = []
        self.update_reserve = []
        self.date_check_in_reserve = []
        self.date_check_out_reserve = []
        self.room_avalible = []

    def add_hotel_list(self,hotel_list):
        self.list_hotel.append(hotel_list)

    def add_date_check_in_reserve(self,date_check_in_reserve):
        self.date_check_in_reserve.append(date_check_in_reserve)
    
    def add_date_check_out_reserve(self,date_check_out_reserve):
        self.date_check_out_reserve.append(date_check_out_reserve)
    
    def add_room_avalible(self,room_avalible):
        self.room_avalible.append(room_avalible)
    

    def select_hotel(self) -> None:
        room_avalible = False
        if type(self.name_hotel) !=str:
            return
        for i in self.list_hotel:
            if i.hotel_name == self.name_hotel:
                print("complete_1")

                for j in  self.date_check_in_reserve :
                    # j is the class in list
                    j.check_in = j.check_in.split("-")
                    # define the attribute in class 
                    for i in j.check_in :
                        j.check_in[j.check_in.index(i)] = int(i)

                for k in self.date_check_out_reserve:
                    # k is the class in list
                    k.check_out = k.check_out.split("-")
                    for i in k.check_out :
                        k.check_out[k.check_out.index(i)] = int(i)

                self.check_in = self.check_in.split("-")
                for i in self.check_in :
                    self.check_in[self.check_in.index(i)] = int(i)

                self.check_out = self.check_out.split("-")
                for i in self.check_out :
                    self.check_out[self.check_out.index(i)] = int(i)

                if self.check_in[0] == self.date_check_in_reserve[0].check_in[0]:
                    if not (self.date_check_in_reserve[0].check_in[1] <= self.check_in[1] <= self.date_check_out_reserve[0].check_out[1]):
                        # if not (self.date_check_in_reserve[0].check_in[0] < self.check_out[0] <= self.date_check_out_reserve[0].check_out[0]):
                        print("complete_2")
                    else:
                        print("fail")

                if not (self.num_people / self.num_room <= 0.25):
                    print("complete_3")
                    room_avalible = True

class Admin:
    def __init__(self, name, email, phone) -> None:
        self.name = name
        self.email = email
        self.phone = phone

class Customer:
    def __init__(self, name, email, phone) -> None:
        self.name = name
        self.email = email
        self.phone = phone        

class Hotel:
    def __init__(self, roomtype, ) -> None:
        pass
    
booking = Booking("hotel","3-25-2023","3-28-2023",2,2)
hotel1 = HotelList("hotel")
reserve1 = Reservedatein("3-21-2023")
reserve2 =Reservedateout("3-25-2023")
roomavalible = RoomAvalible()

booking.add_date_check_in_reserve(reserve1)
booking.add_date_check_out_reserve(reserve2)        
booking.add_hotel_list(hotel1)
booking.add_room_avalible(roomavalible)
booking.select_hotel()

print(booking.list_hotel)

