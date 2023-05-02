from fastapi import FastAPI,status
from starlette.middleware.cors import CORSMiddleware
from fastapi import Request,HTTPException,Depends
from fastapi import responses
from fastapi import status
from datetime import datetime
from pydantic import BaseModel



from model import (insert_register,
   insert_login,
   insert_reserve,
   insert_booking,
   insert_addon,
   insert_debit,
   insert_formaddhotel,
   insert_formaddroom,
   insert_formaddaddon)



app = FastAPI()
app.state.restart_requested = False

origins =[
    'http://localhost:3000',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

@app.get("/data")
async def root():
   return {"message":"hello goodbye"} 



class User:
    def __init__(self,data_user):
        self.data_set = {}
        self.data_set.update(data_user)
        self.__data_user = list(self.data_set.values())
        self.__name = self.__data_user[0]
        self.__email = self.__data_user[1]
        self.__password = self.__data_user[2]
        self.__phone = self.__data_user[3]
        self.__address = self.__data_user[4]

    @property
    def name(self):
        return self.__name
    
    @property
    def email(self):
        return self.__email
    
    @property
    def password(self):
        return self.__password
    
    @property
    def phone(self):
        return self.__phone
    
    @property
    def address(self):
        return self.__address   


class Admin:
    def __init__(self):
        self.__email = "admin@gmail.com"
        self.__password = "0123456789"
        self.__auth = "true"
    

    @property
    def auth(self):
        return self.__auth
    
    @property
    def email(self):
        return self.__email
    
    @property
    def password(self):
        return self.__password

class Collectuser:
    collect = []

class Register:

    def update(self, data, collect):
        if(self.check_update(data,collect)):
            collect.append(data)
            print(self.__user_dict)
            return  {'message':'success'}
        print(self.__user_dict)
        return  {'message':'fail'}
    
    def check_update(self,data,collect):
        for check in collect:
            if check.email == data.email or check.password == data.password:
                print("invalid register")
                return 0
        print("Success register")
        return 1
        
class Login:
    def __init__(self, data):
        self.__data_set = {}
        self.__data_set.update(data)
        self.__data_list = list(self.__data_set.values())
        self.__user_email = self.__data_list[0]
        self.__user_password = self.__data_list[1]
        self.__user_name = ""
    
    def check_login(self, data_collect, admin):
        if self.__user_email == admin.email and self.__user_password == admin.password:
                print("Success auth admin!!")
                return {
                        "auth": admin.auth,
                        "success": "true"
                        }
        for check in data_collect:
            if check.email == self.__user_email and check.password == self.__user_password:
                print("Success login!!")
                self.__user_name = check.name
                return self.show_detail()
        print("invalid login")
        return {"message":"fail"}
        
    def show_detail(self):
        view_account = {
            "name" : self.__user_name,
            "email" : self.__user_email,
            "auth" : "false",
            "success": "true"
        }
        return view_account
    

# Order file !!!!!!!!!!!!!!!!!!!!!!!!!!!

class OrderHistory:
    history = []
    
    def show_history(self):
        for history in self.history:
            print("Date check in :",history.check_in, 
                  "Date check out:",history.check_out, 
                  "Number people:",history.num_people, 
                  "Total room:",history.num_room, 
                  "Hotel name:",history.hotel_name, 
                  "Room number:",history.room_number)
        
            
order_history = OrderHistory()


# Hotel file !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


class Hotel:
    def __init__(self, name_hotel, rating, num_rooms, hotel_picture, location, province):
        self.__name_hotel = name_hotel
        self.__rating = rating
        self.__num_rooms = num_rooms
        self.__hotel_picture = hotel_picture
        self.__location = location
        self.__province = province
        self.__room_list = []
        self.__add_on_hotel = []

     
    def add_room(self, room):
        self.__room_list.append(room)
        
    def add_addons(self,add_on):
        self.__add_on_hotel=add_on
    
    def show_room(self):
        list_set = []
        for room in self.__room_list:
            item = {"roomnum":room.get_room_number, "Type":room.get_room_type,"numpeople":room.get_max_people,
                "price":room.get_price_room, "facs":room.get_facilities_detail, "bedtype":room.get_bed_type,
                "picture":room.get_room_picture,"status":room.get_room_status}
            list_set.append(item)
        return list_set
    
    @property    
    def get_name_hotel(self):
        return self.__name_hotel
    @property
    def get_rating(self):
        return self.__rating
    @property
    def get_num_rooms(self):
        return self.__num_rooms
    @property
    def get_hotel_picture(self):
        return self.__hotel_picture
    @property
    def get_location(self):
        return self.__location
    @property
    def get_province(self):
        return self.__province
    @property
    def get_room_list(self):
        return self.__room_list
    @property
    def get_add_on_hotel(self):
        return self.__add_on_hotel
        
class HotelCatalog:
    hotel_list = []

    def __init__(self) -> None:
        self.__name = ""
        self.__check_in = "" 
        self.__check_out = ""
        self.__num_people = 0

        
    def add_hotel(self):
        # self.__check_awail
        print(self.__check_awail)
        return self.__check_awail
        
    @property
    def getter_name(self):
        return self.__name
    @property
    def getter_checkin(self):
        return self.__check_in
    @property
    def getter_checkout(self):
        return self.__check_out
    @property
    def getter_checkpeople(self):
        return self.__num_people


    def find_hotel(self, name, list_hotel):
        for hotel in list_hotel:
            if hotel.get_name_hotel == name:
                print("access")
                return hotel
        print("Error: Hotel not found")
        
    def find_available_room(self,data, list_hotel):
        self.__hotel_set ={}
        self.__hotel_set.update(data)
        self.__check_awail = list(self.__hotel_set.values())
        self.__name = str(self.__check_awail[1])
        self.__check_in = str(self.__check_awail[4])
        self.__check_out = str(self.__check_awail[5])
        self.__num_people = int(self.__check_awail[3])
        self.__available_rooms = []
        check = 0
        self.__available_rooms_dict ={}
        self.check_in = datetime.strptime(self.__check_in, '%d-%m-%Y').date()
        self.check_out = datetime.strptime(self.__check_out, '%d-%m-%Y').date()
        self.num_people = self.__num_people
        hotel = self.find_hotel(self.__name, list_hotel)
        if hotel:
            for room in hotel.get_room_list:
                check+=1
                available = True
                if self.num_people > room.get_max_people:
                    continue  # skip room if num_people > max_people
                for booking in order_history.history:
                    if  str(booking.hotel_name) == str(self.__name) and int(booking.room_number) == int(room.get_room_number):
                            # Check if the booking overlaps with the given dates
                            if self.check_out > booking.check_in and self.check_in < booking.check_out:
                                available = False 
                                
                if available == True:
                        if available == True and room.get_room_status == False:
                            room.get_room_status = True
                    # Check if the room is available for the given dates
                    
                        self.__available_rooms.append(room)
                        self.__available_rooms_dict.update({f"Number{check}":room.get_room_number,f"Type{check}":room.get_room_type,f"Price{check}":room.get_price_room})

                        print("Room number:",room.get_room_number, "Type:",room.get_room_type, "Max_people:",room.get_max_people,
                              "Price:",room.get_price_room, "Facilities:",room.get_facilities_detail,"Room picture:",room.get_room_picture,
                              "Bed type:",room.get_bed_type, "Status:",room.get_room_status)
            if  len(self.__available_rooms) <= 0:
                print("No room available")
                return {"No room available":"NO"}
            return self.__available_rooms_dict
        else:
            return {"No hotel available":"NO"}
        

    def find_add_on(self,hotel_name, list_hotel):
        hotel = self.find_hotel(hotel_name, list_hotel)
        list_set = []
        if hotel:
            for add_on in hotel.get_add_on_hotel:
                item={"Hotel":hotel.get_name_hotel,"Service_type":add_on.type_service,"Name":add_on.name_service, "Detail":add_on.detail,
                      "Picture":add_on.picture ,"Price":add_on.price_service}
                list_set.append(item)
            return list_set
        return {"message":"fail"}
            
    def show_hotel(self, hotellist):
        list_set = []
        for hotel in hotellist:
            item = {"Name_hotel":hotel.get_name_hotel, "Rating":hotel.get_rating,"Num_rooms":hotel.get_num_rooms,
                "hotel_picture":hotel.get_hotel_picture, "Location":hotel.get_location, "Province":hotel.get_province}
            list_set.append(item)
        return list_set





# Room file !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

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
    @get_room_status.setter
    def get_room_status(self, sets):
        self.__room_status =sets



# Addons file !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

class Addons:
    def __init__(self):
        self.add_on_list  =[]
        self.add_on_price = 0

    def add_service(self, service):
        self.add_on_list.append(service)
        print(self.add_on_list)
    
    def get_add_on_list(self):
        print(self.add_on_list)
        return self.add_on_list
        
   
    def set_add_on_price(self, type_service:str, name_service:str):
        for add_on in self.add_on_list:
            if type_service == add_on.type_service and name_service == add_on.name_service:
                self.add_on_price = add_on.price_service
                #print(self.__add_on_price)
                print(self.add_on_price)
                return self.add_on_price
        else:
            print(self.add_on_price)
    

class Service:
    def __init__(self,type_service,name_service,detail,picture,price_service):
        self.__type_service = type_service
        self.__name_service = name_service
        self.__detail = detail
        self.__picture = picture
        self.__price_service = price_service
    @property
    def type_service(self):
        return self.__type_service
    @property
    def name_service(self):
        return self.__name_service
    @property
    def detail(self):
        return self.__detail
    @property
    def picture(self):
        return self.__picture
    @property 
    def price_service(self):
        return self.__price_service 
     



# Booking file !!!!!!!!!!!!!!!

class Booking:
    def __init__(self, check_in:str, check_out:str, num_people:int, num_room:int):
        self.data_set = {}
        self.data_set.update(num_room)
        self.__data_user = list(self.data_set.values())
        self.check_in = datetime.strptime(check_in, '%d-%m-%Y').date()
        self.check_out = datetime.strptime(check_out, '%d-%m-%Y').date()
        self.num_people = num_people
        self.num_room = self.__data_user[0]
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
        return {"total_price":self.total_price,"message":"success"}

 
    def book_room_check(self, hotel_name, catalog):
        check_catalog = catalog.hotel_list
        hotel = catalog.find_hotel(hotel_name, check_catalog)
        if hotel:
            
            for room in hotel.get_room_list:
                if int(room.get_room_number) == self.num_room :
                    # Check if room is available for given dates    
                                             
                        self.hotel_name = hotel_name
                        self.room_number = self.num_room
                        room.update_status(hotel)
                        self.get_num_days()
                        
                        self.room_price =room.set_room_price(self.total_days)
                        self.set_total_price()

                        return {"message": "Booking successful","Room number": self.num_room, "Room Status": room.get_room_status, "Price":self.total_price}
            else:
                return "Room not found"
        else:
            return "Hotel not found"

    def book_add_on(self, service_type, name_service, catalog):
        hotel = catalog.find_hotel(self.hotel_name, catalog.hotel_list)
        if hotel:
                
            for add_on in hotel.get_add_on_hotel:
                    if add_on.name_service == name_service and add_on.type_service == service_type:
                        
                        self.add_on_price = addons.set_add_on_price(service_type,name_service)
                        self.set_total_price()
                        return {"message": "success", "service_type": service_type, "service_detail": name_service, "price": self.add_on_price}
                    else:
                        self.add_on_price = 0
                        self.set_total_price()
                        return {"message": "success","price": self.add_on_price}
            else:
                self.add_on_price = 0
                self.set_total_price()
                return {"message": "success","price":self.add_on_price}
        else:
            print("Unable to find hotel")


# Payment file !!!!!!!!!!!!!!


class Payment:
    def __init__(self, transaction_id : int):
        self.transaction_id = transaction_id
        self.status_payment = False
        self.total_day = 0
        self.total_price = 0

    def set_booking_details(self, booking):
        self.total_day = booking.total_days
        self.total_price = booking.total_price
        return {"Total days":self.total_day,"Result":self.total_price}
    

     
    def process_payment(self, booking,card_number, card_cvv,all_debit_cards, promotion, pass_coupon):
        print("Process Payment...........")
        print("......")
        print("...")
        self.set_booking_details(booking)
        card_balance = all_debit_cards.check_card_from_user(card_number, card_cvv)
        if card_balance is None:
            return {"message": "Debit card not found"}

        if card_balance < self.total_price:
            return {"message": "Insufficient balance"}

        self.status_payment = True
        self.use_coupon(pass_coupon, promotion)
        card_balance -= self.total_price #money in card
        all_debit_cards.update_card_balance(card_number,card_cvv,card_balance)
        return {"message": "Payment processed successfully", "new_balance": card_balance}
        
    def use_coupon(self, pass_coupon , promotion):
        
        for coupon in promotion.total_coupon:
            if coupon.name_coupon == pass_coupon:
                print("pre total price:",self.total_price)
                self.total_price  -= coupon.value_coupon
                print("post total price:",self.total_price)
                return self.total_price
            
    




class DebitCardModel:
    def __init__(self , number, name, surname, cvv, balance) -> None:
        self.card_number = number
        self.card_name = name
        self.surname = surname
        self.card_cvv = cvv 
        self.card_balance = balance

class AllDebitcard:
    def __init__(self):
        self.__debitcard_list = []

    def add_card(self, card : DebitCardModel): #done
        self.__debitcard_list.append(card)

    def check_card_from_user(self, cardnumber : int, cvv : int):
        for i in self.__debitcard_list:
            if i.card_number == cardnumber and i.card_cvv == cvv:
                return i.card_balance
            

    def update_card_balance(self, card_number, card_cvv, new_balance):
        for debitcard in self.__debitcard_list:
            if debitcard.card_number == card_number and debitcard.card_cvv == card_cvv:
                debitcard.card_balance = new_balance
                break
    
    @property
    def get_debitcard_list(self):
        return self.__debitcard_list


class TypeCoupon:
    def __init__(self, name, desc, value) -> None:
    
        self.name_coupon= name
        self.coupon_description= desc
        self.value_coupon= value


class Promotion:
    def __init__(self):
        self.total_coupon= [] #list of Typecoupon

    def add_coupon(self, coupon:TypeCoupon):
        self.total_coupon.append(coupon)

    def get_coupon_list(self):
        return self.total_coupon


admin=Admin()


room1 = Room(101, 'Standard', 3, 1000, 'TV, AC', 'Queen', "",True)
room2 = Room(102, 'Deluxe', 3, 2000, 'TV, AC, Jacuzzi', 'King', "",True)
room3 = Room(103, 'Standard', 3, 1500, 'TV, AC', 'King', "",True)

hotela = Hotel("Hotel A", "4.9", 10, "https://media-cdn.tripadvisor.com/media/photo-s/26/9d/77/93/entrance-hotel-artemide.jpg", "Puket", "..")
hotelb = Hotel("Hotel B", "4.4", 10, "https://image-tc.galaxy.tf/wijpeg-2w1lrozu9m6gg4myhkj0lkgvf/43-hotel-exterior-v2-resized.jpg?width=1920", "Rayong", "..")
hotelc = Hotel("Hotel C", "4.7", 10, "https://media-cdn.tripadvisor.com/media/photo-s/16/1a/ea/54/hotel-presidente-4s.jpg", "chaingmai", "..")
hoteld = Hotel("Hotel D", "4.2", 10, 'https://pix10.agoda.net/hotelImages/124/1246280/1246280_16061017110043391702.jpg?ca=6&ce=1&s=1024x768', "Bankok", "..")
hotela.add_room(room1)
hotela.add_room(room2)
hotela.add_room(room3)
hotelb.add_room(room1)
hotelb.add_room(room2)
hotelb.add_room(room3)
hotelc.add_room(room1)
hotelc.add_room(room2)
hotelc.add_room(room3)
hoteld.add_room(room1)
hoteld.add_room(room2)
hoteld.add_room(room3)

catalog_hotel = HotelCatalog()
catalog_hotel.hotel_list.append(hotela)
catalog_hotel.hotel_list.append(hotelb)
catalog_hotel.hotel_list.append(hotelc)
catalog_hotel.hotel_list.append(hoteld)




addons =Addons()

servicefood = Service("Breakfast","steak","...","...",100)
servicecar = Service("Carservice","car","...","...",200)
servicespa = Service("Spaservice","spa","...","...",150)

addons.add_service(servicefood)
addons.add_service(servicecar)
addons.add_service(servicespa)
hotela.add_addons(addons.get_add_on_list())
hotelb.add_addons(addons.get_add_on_list())
hotelc.add_addons(addons.get_add_on_list())
hoteld.add_addons(addons.get_add_on_list())

debit1 = DebitCardModel(123, "test", "ttt", 555, 10000)

alldebitcard = AllDebitcard()
alldebitcard.add_card(debit1)

coupon1 = TypeCoupon("cost","...",500)
promotion1 = Promotion()
promotion1.add_coupon(coupon1)

addaddons = Addons()


    


@app.get("/showhotel")
async def showhotel():
    response = catalog_hotel.show_hotel(catalog_hotel.hotel_list)
    # return responses.JSONResponse(response)
    return response

@app.get("/showroom")
async def showroom():
    response = hotel.show_room()    
    return response

# @app.get("/showroomfilter")
# async def Showroomfilter():
#     response = hotel.show_room()    
#     return response

@app.post("/register",response_model=insert_register)
async def register(Insert_register : insert_register):
   # user = User(Insert_register)
   # user.process_data()
   collect_user = Collectuser()
   user =User(Insert_register)
   register =Register()
   response = register.update(user, collect_user.collect)
   print(collect_user.collect)
   if response:
      return responses.JSONResponse(response)
   else:
      raise HTTPException(status_code=400, detail="Something error")

   
@app.post("/login",response_model=insert_login,status_code=status.HTTP_200_OK)
async def login(Insert : insert_login):
      collect_user = Collectuser()
      login = Login(Insert)
      global responselogin
      responselogin = login.check_login(collect_user.collect, admin)
      if responselogin:
         return responses.JSONResponse(responselogin)

@app.get("/auth")
async def auth():
    if responselogin:
        return  {"message":"success"}
    return {"message":"fail"}

@app.post("/managehotel",response_model=insert_formaddhotel,status_code=status.HTTP_200_OK)
async def manage_hotel(Insert_form : insert_formaddhotel):
    set_data = {}
    set_data.update(Insert_form)
    set_data_list = list(set_data.values()) 
    hotel_add = Hotel(set_data_list[0], set_data_list[1], set_data_list[2], set_data_list[3], set_data_list[4],set_data_list[5])
    catalog_hotel.hotel_list.append(hotel_add)
    print(catalog_hotel.hotel_list)
    response = {"message":"success"}
    return responses.JSONResponse(response)

@app.post("/manageroom",response_model=insert_formaddroom,status_code=status.HTTP_200_OK)
async def manage_room(Insert_form : insert_formaddroom):
    set_data = {}
    set_data.update(Insert_form)
    set_data_list = list(set_data.values())
    room_add = Room(set_data_list[1], set_data_list[2], set_data_list[3], set_data_list[4], set_data_list[5], set_data_list[6], set_data_list[7], set_data_list[8])
    global hotel
    hotel = catalog_hotel.find_hotel(set_data_list[0], catalog_hotel.hotel_list)
    hotel.add_room(room_add)
    print(hotel.get_room_list)
    response = {"message":"success"}
    return responses.JSONResponse(response)

@app.get("/getaddons")
async def getaddonss():
    return response_filter_addons



@app.post("/manageaddons",response_model=insert_formaddaddon,status_code=status.HTTP_200_OK)
async def manage_addon(Insert_form : insert_formaddaddon):        
    set_data = {}
    set_data.update(Insert_form)
    set_data_list = list(set_data.values())
    add_data_addon = Addons()
    service = Service(set_data_list[0], set_data_list[1], set_data_list[2], set_data_list[3], set_data_list[4])
    add_data_addon.add_service(service)
    hoteladdons = catalog_hotel.find_hotel(set_data_list[5], catalog_hotel.hotel_list)
    hoteladdons.add_addons(add_data_addon.get_add_on_list())
    global response_filter_addons
    response_filter_addons = catalog_hotel.find_add_on(set_data_list[5], catalog_hotel.hotel_list)
    response = {"message":"success"}
    return responses.JSONResponse(response)



    # type_service,name_service,detail,picture,price_service
    # return {""}




@app.post("/findavailableroom",response_model=insert_reserve,status_code=status.HTTP_200_OK)
async def reserve(Insert_reserve : insert_reserve):
    print(catalog_hotel.hotel_list)
    global response
    response = catalog_hotel.find_available_room(Insert_reserve,
    catalog_hotel.hotel_list)
    global name
    global check_in
    global check_out
    global check_people
    name = catalog_hotel.getter_name
    check_in = catalog_hotel.getter_checkin
    check_out = catalog_hotel.getter_checkout
    check_people = catalog_hotel.getter_checkpeople
    

    # book = Booking(ci, co, cp, 1)
    print(response)
    if response:
        return responses.JSONResponse(response)
    else:
      raise HTTPException(status_code=400, detail="Something error")

# check_in:str, check_out:str, num_people:int, num_room:int

# check_in:str, check_out:str, num_people:int, num_room:int

@app.post("/findaddon",response_model=insert_booking,status_code=status.HTTP_200_OK) #find add on
async def findaddon(Insert_booking : insert_booking):
    global book
    book = Booking(check_in, check_out, check_people, Insert_booking)
    global response_filter_addons
    response_filter_addons = catalog_hotel.find_add_on(name, catalog_hotel.hotel_list)
    response= {"message":"true"}
    
    return responses.JSONResponse(response)

@app.get("/bookroom")  #booking
async def book_room():
    response    = book.book_room_check(name, catalog_hotel)
    print(response)
    return responses.JSONResponse(response)


@app.post("/addon",response_model=insert_addon,status_code=status.HTTP_200_OK)
async def bookadd_on(Insert_addon : insert_addon):
    setup = {}
    setup.update(Insert_addon)
    setupp = list(setup.values())
    response=book.book_add_on(setupp[0], setupp[1], catalog_hotel)
    
    
    return responses.JSONResponse(response)

@app.get("/totalprice")
async def total_price():
    response = book.set_total_price()
    return responses.JSONResponse(response)

@app.post("/payment",response_model=insert_debit,status_code=status.HTTP_200_OK)
async def payment( Insert_debit: insert_debit):
    setup = {}
    setup.update(Insert_debit)
    setupp = list(setup.values())
    alldebitcard.check_card_from_user(setupp[0],setupp[1])
    pay = Payment(123456)
    global responsebill
    responsebill =pay.process_payment(book, setupp[0], setupp[1], alldebitcard, promotion1, setupp[2])
    print(responsebill)
    return responses.JSONResponse(responsebill)
    
@app.get("/bill")
async def show_bill():
    return responses.JSONResponse(responsebill)

@app.get("/updatebill")
async def Updatehistory():
    order_history.history.append(book)
    #print(order_history)
    order_history.show_history()
    response = {"message":"success"}
    return responses.JSONResponse(response)





    


          

   





