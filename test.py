from fastapi import FastAPI

app = FastAPI()
class Hotel:
    def __init__(self, name, rating, num_rooms, hotel_picture, location, province, hotel_room_list, add_on_hotel):
        self.name_hotel = name
        self.rating = rating
        self.num_rooms = num_rooms
        self.hotel_picture = hotel_picture
        self.location = location
        self.province = province
        self.room_list = hotel_room_list
        self.add_on_hotel = add_on_hotel

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
    
    
class HotelCatalog:
    def __init__(self):
        self.hotel_list = []
        

    def add_hotel(self, hotel):
        self.hotel_list.append(hotel)

    @app.get("/hotel")
    async def find_hotel(self, name):
        for hotel in self.hotel_list:
            if hotel.name_hotel == name:
                return {"hotel_llist": hotel}
            else:
                return {"hotel_list": None}

    
class Room():
    def __init__(self, room_number, room_type, max_people, price_room, facilities_detail, bed_type, status):
        self.room_number = room_number
        self.room_type = room_type
        self.max_people = max_people
        self.price_room = price_room
        self.facilities_detail = facilities_detail
        self.bed_type = bed_type
        self.room_status = status
    
    def update_status(self, hotel, room_catalog:object):
        self.room_status = not self.room_status
        self.room_catalog = room_catalog
        for room in hotel.room_list:
            if room.room_number == self.room_number:
                room.room_status = self.room_status
                break
        
        for i, room in enumerate(self.room_catalog.room_list):
            if room[0] == self.room_number:
                updated_room = (self.room_number, self.room_type, self.max_people, self.price_room, self.facilities_detail, 
                                self.bed_type, self.room_status)
                room_cat.room_list[i] = updated_room
                break
        
    
                
# Define the class to add the new list to

class AvailableRoom:
    def __init__(self):
        self.room_list = []
    def add_room(self, room_class):
        new_room = (room_class.room_number, room_class.room_type, room_class.max_people, room_class.price_room, room_class.facilities_detail, 
                    room_class.bed_type, room_class.room_status)
        if new_room[6] == True:
            self.room_list.append(new_room)
    
    def remove_room(self):
        for i in self.room_list:
            if i[6] == False:
                self.room_list.pop(self.room_list.index(i))
        

    
        
    



class Addons:
    def __init__(self):
        self.add_on_list  =[]
    
    def add_breakfast_service(self, breakfast):
        breakfast_list=(breakfast.type_service, breakfast.detail ,breakfast.type_food, breakfast.price_food)
        self.add_on_list.append(breakfast_list)

    def add_spa_service(self, spa):
        spa_list=(spa.type_service, spa.detail, spa.spa_picture, spa.price_spa)
        self.add_on_list.append(spa_list)
    
    def get_add_on_list(self):
        return self.add_on_list

class BreakfastService():
    def __init__(self, type_service, detail, type_food, price_food):
        self.type_service = type_service
        self.detail = detail
        self.type_food = type_food
        self.price_food = price_food
   

class SpaService:
    def __init__(self, type_service, detail, spa_picture, price_spa):
        self.type_service = type_service
        self.detail = detail
        self.spa_picture = spa_picture
        self.price_spa = price_spa

class ActivityService:
    def __init__(self, type_service, detail, date_activity, num_person, price_activity):
        self.type_service = type_service
        self.detail = detail
        self.data_activity = date_activity
        self.num_person = num_person
        self.price_activity = price_activity

class TaxiService:
    def __init__(self, type_service, detail,number_taxi, fees_taxi, contact_taxi):
        self.type_service = type_service
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

        self.service_price = 0 
        
    
    
    def book_room_check(self, hotel_name, room_number):
        hotel = catalog.find_hotel(hotel_name)
        self.chosen_hotel = hotel_name
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
                            room.update_status(hotel,room_cat) #update_status
                            room_cat.remove_room()
                            
                            
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
                            self.booking_add_on() #after book room complete
                            return True
                        else:
                            print("fail")
                            print("Unable to book room.")
                            return False
                            
            print("Unable to find room")
        else:
            print("Unable to find hotel.")

   
    def booking_add_on(self,  choices=["breakfast","spa","activity","taxi"]):
            hotel = catalog.find_hotel(self.chosen_hotel)
            hotel.show_add_on()
            filtered_list = [] #collect service type in hotel
            print("Do you want addon")
            requirement = input("True or False:")
            if requirement == "True":
                if hotel:
                    add_on_cat = hotel.add_on_hotel[0]              #list of add_on in hotel
                    type_input = input("Enter type_service :[breakfast,spa,activity,taxi]")
                    for item in add_on_cat.add_on_list :                         
                        if item[0] == type_input and type_input in choices: #watch first index breakfast spa activity taxi
                            filtered_list.append(item)                     #ใส่เฉพาะ type_service ที่กรอก input  
                    if len(filtered_list) > 0:                             # Not []
                        for index, item in enumerate(filtered_list):     
                            print("choice:",str(index+1),item[1])          #show index 1 of each filter serviece ex.breakfast service -> corn_soup ,sisler sald   
                    if item[0] == type_input and type_input in choices:
                        choice = int(input("enter your choice:"))
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
        self.__used_coupons = []
        self.__total_day = 0
        self.__total_price = 0
        self.__add_on_price = 0
    
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
    
    def set_total_day(self, booking:object):
        self.booking = booking
        self.__total_day += self.booking.total_day
        print("Total day:",self.__total_day)

    def set_add_on_price(self, booking:object):
        self.booking = booking
        self.__add_on_price = self.booking.service_price
        print("Add on price:",self.__add_on_price)

    def set_total_price(self):
        self.__total_price = (self.__price_room * self.__total_day) + self.__add_on_price
        print("Total price:",self.__total_price)


    def use_coupon(self, promotion_instance):
        self.promotion = promotion_instance
        print("Do you want to use coupon:")
        requirement = input("True or False:")
        if requirement == "True":
            name_coupon = input("Enter coupon code:")
            for coupon in self.promotion.total_coupon:
                if coupon.name_coupon == name_coupon:
                    self.__total_price  -= coupon.value_coupon
                    break
            else:
                print("Invalid coupon name")
        else: 
            print("Not use coupon")

    def process_payment(self):
        print("Process Payment...........")
        print("......")
        print("...")
        if(self.__money >= self.__total_price): #price_room must multiply day checkout-checkin

            if self.use_coupon(promotion):
                print("Total after use coupon code:",self.__total_price)
            
            print("Success Payment!!")
            self.__money-=self.__total_price
            self.__status_payment = True
            print("Payment status is True")
            print("Your Balance is",self.__money)
            return True
        else:
            print("Fail Payment")
            return False



class Promotion:
    def __init__(self):
        self.total_coupon= [] #list of Typecoupon
        self.total_discount_num_room_list = [] #list of discountnumroom

    def add_coupon(self, coupon):
        self.total_coupon.append(coupon)

    def show_coupon_list(self):
        for discount in self.total_coupon:
            print("Total Coupon:",self.total_coupon)
    
    def get_coupon_list(self):
        return self.total_coupon
                


class TypeCoupon:
    def __init__(self, name_coupon, coupon_description, value_coupon):
        self.name_coupon = name_coupon
        self.coupon_description=coupon_description
        self.value_coupon = value_coupon

   

class DiscountNumRoom:
    def __init__(self, num_room_discount, value_discount):
        self.num_room_discount = num_room_discount
        self.value_discount = value_discount

room_cat = AvailableRoom()
room1 = Room(101, 'Standard', 3, 1000, 'TV, AC', 'Queen', True)
room2 = Room(102, 'Deluxe', 3, 2000, 'TV, AC, Jacuzzi', 'King', True)
room3 = Room(103, 'Deluxe', 4, 3000, 'TV, AC, Jacuzzi', 'Queen', True)

room_cat.add_room(room1)
room_cat.add_room(room2)
room_cat.add_room(room3)

print(room_cat.room_list)

add_on_cat = Addons()
breakfast1 = BreakfastService("breakfast","corn soup","soup", 100)
breakfast2 = BreakfastService("breakfast","sisler salad","salad",120)
spa1 = SpaService("spa","Open 9am","picture",100)
add_on_cat.add_breakfast_service(breakfast1)
add_on_cat.add_spa_service(spa1)
add_on_cat.add_breakfast_service(breakfast2)


add_on_cat2 = Addons()
breakfast3 = BreakfastService("breakfast","sisler-salad","salad", 100)
breakfast4 = BreakfastService("breakfast","oishi buffe","buffe",350)
add_on_cat2.add_breakfast_service(breakfast3)
add_on_cat2.add_breakfast_service(breakfast4)


hotel1 = Hotel('Hotel A', 5, 2, "A", "Lardprao", "Bangkok", [room1, room2],[add_on_cat])
hotel2 = Hotel('Hotel B', 5, 2, "A", "Lardprao", "Bangkok", [room1, room2],[add_on_cat2])
# create a hotel catalog and add the hotel
catalog = HotelCatalog()
catalog.add_hotel(hotel1)
catalog.add_hotel(hotel2)
print("before booking")
hotel1.show_hotel(catalog)
print("Room list:",room_cat.room_list)
hotel1.show_room()


book1=Booking(room_cat,"13-3-2021","15-3-2021",3,1)

book1.book_room_check("Hotel A", 101)
print("Room list:",room_cat.room_list)

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

coupon = TypeCoupon("coupon A","discount 100 bath",100)
promotion = Promotion()
promotion.add_coupon(coupon)

pay1 = Payment( 457123450, credit1)
pay1.set_money(credit1.get_balance_in_card())
pay1.set_price_room(room1.price_room)
print("Price room "+str(room1.room_number)+" is "+str(pay1.get_price_room())+" bath")
print("##Before Process Payment")
print("Payment status is ",pay1.get_payment_status())

pay1.set_total_day(book1)
pay1.set_add_on_price(book1)
pay1.set_total_price()

pay1.process_payment()

#book second time 
book2=Booking(room_cat,"20-3-2021","25-3-2021",3,1)
book2.book_room_check("Hotel B", 101)


