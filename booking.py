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
    def __init__(self, room_catalog, check_in, check_out, num_people, num_room):
        self.room_catalog = room_catalog
        self.num_people =  num_people
        self.num_room = num_room
        self.check_in = check_in
        self.check_out = check_out
        self.date_check_in_reserve = ["Hotel A-101-21-3-2021","Hotel B-101-19-3-2021","Hotel B-102-13-3-2021"]
        self.date_check_out_reserve = ["Hotel A-101-23-3-2021","Hotel B-101-26-3-2021","Hotel B-102-15-3-2021"]
        self.check_hotel = []
        self.check_room = []

    def get_room_list(self):
        return self.room_catalog.room_list
    
    
    def book_room_check(self, hotel_name, room_number):
        hotel = catalog.find_hotel(hotel_name)
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
                                    if(hotel_name[6]==j):
                                        state_check_in = i.split("-")
                                        room_in=int(state_check_in[1])
                                        day_in=int(state_check_in[2])
                                        month_in=int(state_check_in[3])
                                        year_in=int(state_check_in[4])
                                        for k in self.date_check_out_reserve:
                                            for n in k:
                                                if(n==k[6]):
                                                    if(hotel_name[6]==n):
                                                        state_check_out = i.split("-")
                                                        day_out=int(state_check_out[2])
                                                        month_out=int(state_check_out[3])
                                                        year_out=int(state_check_out[4])
                                                        if self.check_in[1] == month_in and int(room_in) == int(room_number):
                                                            if not (day_in<= self.check_in[0] <= day_out) and not(self.num_room / self.num_people <= 0.25):
                                                                status_collect.append(True)         
                                                            else:
                                                                status_collect.append(False)
                        
                        for check in status_collect:
                            value_collect +=1
                            if(check==True):
                                value_check_true+=1

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

                            return True
                        else:
                            print("fail")
                            print("Unable to book room.")
                            return False
                            
            print("Unable to find room")
        else:
            print("Unable to find hotel.")


class Catalog_creditcard:
    def __init__(self):
        self.creditcard_list = ["100-Prayad-456-10000","101-Messi-555-5000","102-John-789-7000","103-Man-858-500"]
        self.card_number_list =[]
        self.card_name_list=[]
        self.cvv_card_list=[]
        self.balance_list =[]
    
    def manage_card(self):
        for i in self.creditcard_list:
            collect = i.split("-")
            self.card_number_list.append(collect[0])
            self.card_name_list.append(collect[1])
            self.cvv_card_list.append(collect[2])
            self.balance_list.append(int(collect[3]))
        

    def add_card(self, card):
        self.creditcard_list.append(card)

    # def find_hotel(self, name):
    #     for hotel in self.hotel_list:
    #         if hotel.name_hotel == name:
    #             return hotel
    #     print("Error: Hotel not found")
    #     return None

class Creditcard():
    def __init__(self, card_number, card_name, cvv_card):
        self.__card_number = card_number
        self.__card_name = card_name
        self.__cvv_card = cvv_card
        self.__card_number_list = [] #check card num
        self.__card_name_list = [] #check card name
        self.__balance_list = [] #check balance
        self.__balance = 0
        self.__check_status_access = False
        self.__check_end = 0

    def get_card_number(self):
        return self.__card_number
    
    def get_card_name(self):
        return self.__card_name
    
    def get_cvv_card(self):
        return self.__cvv_card
    
    def get_balance_in_card(self):
        return self.__balance
    
    #print check
    def get_data_card_list(self):
        return self.__card_number_list
    
    def receive_data_card(self, check_number, check_name):
        self.__card_number_list += check_number
        self.__card_name_list += check_name

    def check_credit_card(self):
        check_position = -1
        for i in self.__card_number_list:
            check_position +=1
            if(int(i)==int(self.__card_number)):
                print("ACCEPT CREDIT CARD!!")
                self.__check_status_access=True
                self.__check_end = check_position
            else:
                print("ERRORRRRR NOT FOUND NUMBER CARD")
            
    
    def balance_in_card(self, balance):
        position_balance = 0
        if self.__check_status_access:
            position_balance = self.__check_end
            self.__balance += int(balance[position_balance])
            print("Success access balance")
        else:
            print("Error Insert Money!!!!")
    



class Payment:
    def __init__(self, transaction_id, payment_method):
        self.__transaction_id = transaction_id
        self.__payment_method = payment_method
        self.__money = 0 
        # self.__vat
        # self.__total
        self.__price_room = 0
        self.__status_payment =False
    
    def set_price_room(self, price_room):
        if isinstance(price_room,int):
            self.__price_room = price_room
    
    def set_money(self,balance):
        self.__money += balance
    
    def get_price_room(self):
        return self.__price_room

    
    def payment_perform(self):
        pass
    
    
    def get_payment_status(self):
        return self.__status_payment
    
    def process_payment(self):
        print("Process Payment...........")
        print("......")
        print("...")
        if(self.__money >= self.__price_room):
            print("Success Payment!!")
            self.__money-=self.__price_room
            self.__status_payment = True
            print("Payment status is True")
            print("Your Balance is",self.__money)
            return True
        else:
            print("Fail Payment")
            return False



class Promotion:
    def __init__(self, typecoupon, discountnumroom):
        self.__total_coupon= typecoupon #list of Typecoupon
        self.__total_discount_num_room_list = discountnumroom #list of discountnumroo 

class TypeCoupon:
    def __init__(self, value_coupon, pr, coupon_description):
        self.__value_coupon = value_coupon
        self.__pr=pr
        self.__coupon_description=coupon_description

class DiscountNumRoom:
    def __init__(self, num_room_discount, value_discount):
        self.__num_room_discount = num_room_discount
        self.__value_discount = value_discount
    



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
hotel2 = Hotel('Hotel B', 5, 2, "A", "Lardprao", "Bangkok", [room1, room2],[add_on_cat])
# create a hotel catalog and add the hotel
catalog = HotelCatalog()
catalog.add_hotel(hotel1)
catalog.add_hotel(hotel2)
print("before booking")
hotel1.show_add_on()
hotel1.show_room()

book1=Booking(room_cat,"13-3-2021","15-3-2021",3,1)
book1.book_room_check("Hotel B", 101)

hotel1.show_room()

credit_cat = Catalog_creditcard()
credit_cat.manage_card()
# print(credit_cat.card_name_list)
# print(credit_cat.balance_list)

credit1 = Creditcard(101,"Prayut","475-123-568")
credit1.receive_data_card(credit_cat.card_number_list,credit_cat.card_name_list)


credit1.check_credit_card()
credit1.balance_in_card(credit_cat.balance_list)
print("Balance in credit card is "+str(credit1.get_balance_in_card())+" bath")

pay1 = Payment( 457123450, credit1)
pay1.set_money(credit1.get_balance_in_card())
pay1.set_price_room(room1.price_room)
print("Price room "+str(room1.room_number)+" is "+str(pay1.get_price_room())+" bath")
print("##Before Process Payment")
print("Payment status is ",pay1.get_payment_status())

pay1.process_payment()


