from fastapi import FastAPI,status
from starlette.middleware.cors import CORSMiddleware
from fastapi import Request,HTTPException,Depends
from fastapi import responses
from fastapi import status
from datetime import datetime
from pydantic import BaseModel


from model import (insert_register,
   insert_login)



app = FastAPI()

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



class Profile:
    def __init__(self, prefix, name, surname, email, phone_number):
        self._prefix = prefix
        self._name = name
        self._surname = surname
        self._email = email
        self._phone_number = phone_number

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
    def __init__(self, name, id, password):
        self.__id = id
        self.__password = password
        self.__name = name

    @property
    def name(self):
        return self.__name
    
    @property
    def id(self):
        return self.__id
    
    @property
    def password(self):
        return self.__password

class Collectuser:
    collect = []

class Register:
    def __init__(self) -> None:
        self.__user_dict ={}

    def update(self, data, collect):
        # self.__user_dict.update(data)
        # collect.append(self.__user_dict)
        if(self.check_update(data,collect)):
            collect.append(data)
            print(self.__user_dict)
            return  self.__user_dict
        print(self.__user_dict)
        return  self.__user_dict
    
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
    
    def check_login(self, data_collect):
        for check in data_collect:
            if check.email == self.__user_email and check.password == self.__user_password:
                print("Success login!!")
                self.__user_name = check.name
                return self.show_detail()
        print("invalid login")
        return {}
        
    def show_detail(self):
        view_account = {
            "name" : self.__user_name,
            "email" : self.__user_email,
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
            
# order_history = OrderHistory()





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
        self.__add_on_hotel.append(add_on)
    
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

    def __init__(self,data_reserve) -> None:
        self.__hotel_set ={}
        self.__hotel_set.update(data_reserve)
        self.__hotel_list = list(self.__hotel_set.values())
        
    def add_hotel(self, list_hotel):
        list_hotel.append(self.__hotel_list)

    def find_hotel(self, name):
        for hotel in self.__hotel_list:
            if hotel.get_name_hotel == name:
                return hotel
        print("Error: Hotel not found")
        
    def find_available_room(self, hotel_name,check_in, check_out,num_people):
        self.__available_rooms = []
        self.check_in = datetime.strptime(check_in, '%d-%m-%Y').date()
        self.check_out = datetime.strptime(check_out, '%d-%m-%Y').date()
        self.num_people = num_people
        hotel = self.find_hotel(hotel_name)
        if hotel:
            for room in hotel.get_room_list:
                available = True
                if self.num_people > room.get_max_people:
                    continue  # skip room if num_people > max_people
                for booking in order_history.history:
                    if  booking.hotel_name == hotel_name and booking.room_number == room.get_room_number:
                            # Check if the booking overlaps with the given dates
                            if self.check_out > booking.check_in and self.check_in < booking.check_out:
                                available = False 
                                
                if available == True:
                        if available == True and room.get_room_status == False:
                            room.get_room_status = True
                    # Check if the room is available for the given dates
                    
                        self.__available_rooms.append(room)
                        print("Room number:",room.get_room_number, "Type:",room.get_room_type, "Max_people:",room.get_max_people,
                              "Price:",room.get_price_room, "Facilities:",room.get_facilities_detail,"Room picture:",room.get_room_picture,
                              "Bed type:",room.get_bed_type, "Status:",room.get_room_status)
            if  len(self.__available_rooms) <= 0:
                print("No room available")
                return {"No room available"}
            return self.__available_rooms
        else:
            return None

    def find_add_on(self,hotel_name):
        hotel = self.find_hotel(hotel_name)
        if hotel:
            for add_on in hotel.get_add_on_hotel:
                print("Hotel name:",hotel_name,"Service type:",add_on.type_service, "Name:",add_on.name_service, "Detail:",add_on.detail,
                      "Picture:",add_on.picture ,"Price:",add_on.price_service)



    def show_hotel(self):
        for hotel in self.__hotel_list:
            print("Name hotel:",hotel.get_name_hotel, "Rating:",hotel.get_rating,"Num_rooms:",hotel.get_num_rooms,
                  "hotel_picture:",hotel.get_hotel_picture, "Location:",hotel.get_location, "Province:",hotel.get_province)

    def get_hotel_list(self):
        return self.__hotel_list


class HotelToAdd(BaseModel):
    name_hotel: str
    rating: int
    num_rooms: int = 10
    hotel_picture: None | str = None
    location: str = "Thailand"
    province: str 
    room_list = []
    add_on_hotel = []
    
    # add function add room
    def add_room(self, room):
        self.room_list.append(room)


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



# Addons file !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

class Addons:
    def __init__(self):
        self.add_on_list  =[]
        self.add_on_price = 0

    def add_service(self, service):
        service_list = (service.type_service,service.name_service,service.detail,service.picture,service.price_service)
        self.add_on_list.append(service_list)
    
    def get_add_on_list(self):
        print(self.add_on_list)
        
   
    def set_add_on_price(self, type_service, name_service):
        for add_on in self.add_on_list:
            if type_service == add_on[0] and name_service == add_on[1]:
                self.add_on_price = add_on[4]
                #print(self.__add_on_price)
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
    def __init__(self, check_in, check_out, num_people, num_room):
        self.check_in = datetime.strptime(check_in, '%d-%m-%Y').date()
        self.check_out = datetime.strptime(check_out, '%d-%m-%Y').date()
        self.num_people = num_people
        self.num_room = num_room
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
        return {"total_price":self.total_price}

 
    def book_room_check(self, hotel_name, room_number, catalog: HotelCatalog, order_history: OrderHistory):
        hotel = catalog.find_hotel(hotel_name)
        if hotel:
            
            for room in hotel.get_room_list:
               
                if room.get_room_number == room_number :
                    # Check if room is available for given dates
                                            
                        self.hotel_name = hotel_name
                        self.room_number = room_number
                        order_history.history.append(self)
                        room.update_status(hotel)
                        self.get_num_days()
                        #self.set_room_price(room)
                        self.room_price =room.set_room_price(self.total_days)
                        self.set_total_price()

                        return {"message": "Booking successful","Room number": room_number, "Room Status": room.get_room_status}
            else:
                return "Room not found"
        else:
            return "Hotel not found"

    def book_add_on(self, service_type, name_service, catalog: HotelCatalog, requirement):
        hotel = catalog.find_hotel(self.hotel_name)
        if hotel:
            if requirement == False:
                return  {"No booking addon"}
            
            add_on_services = []
            for add_on in hotel.get_add_on_hotel:
                if add_on.type_service == service_type:
                    add_on_services.append(add_on)
                    
            if len(add_on_services) >0:
                
                for add_on in add_on_services:
                    if add_on.name_service == name_service:
                        
                        self.add_on_price = add_on_cat.set_add_on_price(service_type,name_service)
                        self.set_total_price()
                        return {"message": "service booked successfully", "service_type": service_type, "service_detail": name_service, "price": self.add_on_price}
                    else:
                        return {"No this service_detail":name_service,"found in hotel":self.hotel_name}
            else:
                return {"No this service_type":service_type,"found in hotel":self.hotel_name}
        else:
            print("Unable to find hotel")







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
      return response
   else:
      raise HTTPException(status_code=400, detail="Something error")

   
@app.post("/login",response_model=insert_login,status_code=status.HTTP_200_OK)
async def login(Insert : insert_login):
      collect_user = Collectuser()
      login = Login(Insert)
      response = login.check_login(collect_user.collect)
      if response:
         return responses.JSONResponse(response)


@app.post("/reserve",response_model=insert_reserve,status_code=status.HTTP_200_OK)
async def reserve(Insert_reserve : insert_reserve):
    catalog_hotel = HotelCatalog(Insert_reserve)
    catalog_hotel.add_hotel(catalog_hotel.hotel_list)
          

   






   
