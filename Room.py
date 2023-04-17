from hotel import HotelCatalog,Hotel,catalog

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

class RoomList:
    def __init__(self):
        self.room_list = []
    
    def add_room(self, room_class):
        new_room = (room_class.room_number, room_class.room_type, room_class.max_people, room_class.price_room, room_class.facilities_detail, 
                    room_class.bed_type, room_class.room_status)
        self.room_list.append(new_room)

class Booking:
    def __init__(self, check_in, check_out, num_people, num_room):
     
        self.num_people =  num_people
        self.num_room = num_room
        self.check_in = check_in
        self.check_out = check_out
        self.date_check_in_reserve = ["Hotel A-101-21-3-2021","Hotel B-101-19-3-2021","Hotel B-102-13-3-2021"]
        self.date_check_out_reserve = ["Hotel A-101-23-3-2021","Hotel B-101-26-3-2021","Hotel B-102-15-3-2021"]
        self.check_hotel = []
        self.check_room = []
        self.service_price = 0 

    
    def book_room_check(self, hotel_name, room_number, catalog: HotelCatalog):
        hotel = catalog.find_hotel(hotel_name) #catalog is hotel catalog
        self.chosen_hotel = hotel_name
        month_in = None
        if hotel:
            for room in hotel.room_list:
                if room.room_number == room_number: #check เลขห้อง
                        
                        self.check_in = self.check_in.split("-")
                        for i in self.check_in :
                            self.check_in[self.check_in.index(i)] = int(i)

                        self.check_out = self.check_out.split("-")
                        for i in self.check_out :
                            self.check_out[self.check_out.index(i)] = int(i)
                        
                        status_collect=[]
                        value_collect =0
                        value_check_true =0
                        
                        for i in self.date_check_in_reserve:
                            for j in i:
                                if(j==i[6]):
                                    if (hotel_name[6]==j):
                                        state_check_in = i.split("-")
                                        room_in=int(state_check_in[1])
                                        day_in=int(state_check_in[2])
                                        month_in=int(state_check_in[3])
                                        year_in=int(state_check_in[4])

                        for k in self.date_check_out_reserve:
                            for n in k:
                                if(n==k[6]):
                                    if (hotel_name[6]==n):
                                        state_check_out = k.split("-")
                                        day_out=int(state_check_out[2])
                                        month_out=int(state_check_out[3])
                                        year_out=int(state_check_out[4])


                        if month_in is not None and self.check_in[1] == month_in and int(room_in) == int(room_number):
                            if not (day_in<= self.check_in[0] <= day_out) and not(self.num_room / self.num_people <= 0.25):
                                status_collect.append(True)
                                        
                            else:
                                status_collect.append(False)
                        
                        for check in status_collect:
                            value_collect +=1
                            if(check==True):
                                value_check_true+=1
                        
                        if (self.check_in[2]%4==0 and self.check_in[2]%100 !=0) or self.check_in[2]%400 == 0:
                                if(self.check_in[1]==2 and 1<=self.check_in[0]<=29):
                                    print("year Atigu")
                                if(self.check_in[1]==2 and (30<=self.check_in[0]<=31 or 30<=self.check_out[0]<=31)):
                                    print("error insert Day")
                                    return False
                        else:
                            if(self.check_in[1]==2 and 1<=self.check_in[0]<=28):
                                print("year Pokkati")
                            if(self.check_in[1]==2 and (29<=self.check_in[0]<=31 or 29<=self.check_out[0]<=31)):
                                print("error insert Day")
                                return False
                                
                        
                        if room.room_status == True and value_check_true==value_collect:
                            room.update_status(hotel) #update_status
                            collect_in = hotel_name+"-"+str(room_number)+"-"+str(self.check_in[0])+"-"+str(self.check_in[1])+"-"+str(self.check_in[2])
                            collect_out = hotel_name+"-"+str(room_number)+"-"+str(self.check_out[0])+"-"+str(self.check_out[1])+"-"+str(self.check_out[2])
                            self.date_check_in_reserve.append(collect_in)
                            self.date_check_out_reserve.append(collect_out)
                            print("##update_checkin....")
                            print(self.date_check_in_reserve)
                            print("##update_checkout...")
                            print(self.date_check_out_reserve)
                            print("Room booked successfully!")
                            print("Room status:",room_number,":",room.room_status) #show status


                            self.total_day = ( int(self.check_out[0]) - int(self.check_in[0]) ) + 30*( int(self.check_out[1]) - int(self.check_in[1]) )
                            if self.total_day ==0:
                                self.total_day +=1
                            print(self.total_day) #send total_day to class Payment
                    
                            room.update_status(hotel) #update_status

                            #self.booking_add_on(catalog) #after book room complete
                            return True
                        else:
                            print("fail")
                            print("Unable to book room.")
                            return False
                            
            print("Unable to find room")
        else:
            print("Unable to find hotel.")

    
    
    def booking_add_on(self,hotel_name, requirement, type_service, choice, catalog: HotelCatalog,  choices=["breakfast","spa","activity","taxi"]):
            hotel = catalog.find_hotel(hotel_name)
            hotel.show_add_on()
            filtered_list = [] #collect service type in hotel
            print("Do you want addon")
            requirement = requirement
            if requirement == "True":
                if hotel:
                    add_on_cat = hotel.add_on_hotel[0]              #list of add_on in hotel
                    type_input = type_service   #"Enter type_service :[breakfast,spa,activity,taxi]
                    for item in add_on_cat.add_on_list :                         
                        if item[0] == type_input and type_input in choices: #watch first index breakfast spa activity taxi
                            filtered_list.append(item)                     #ใส่เฉพาะ type_service ที่กรอก input  
                    if len(filtered_list) > 0:                             # Not []
                        for index, item in enumerate(filtered_list):     
                            print("choice:",str(index+1),item[1])          #show index 1 of each filter serviece ex.breakfast service -> corn_soup ,sisler sald   
                    if item[0] == type_input and type_input in choices:
                        choice = choice                           #"enter your choice:"
                        if choice in range(1,len(add_on_cat.add_on_list)+1):
                            self.result = filtered_list[choice-1]
                            print("Booking addon success")
                            print("Your choice is:",self.result)
                            self.set_add_on_price()
                    else:
                        print("This hotel has no this service type")

                else:
                    print("Unable to find hotel")    
            else:
                print("Add on is not booking")


    

    def set_add_on_price(self):
        self.service_price = self.result[3]
        print(self.service_price)
