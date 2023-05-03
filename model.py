from pydantic import BaseModel

class insert_register(BaseModel):
    name: str
    email:str
    password:str
    phone:str
    address:str

class insert_login(BaseModel):
    email:str
    password:str
    # message:bool

class insert_reserve(BaseModel):
    country:str
    hotel:str
    room:str
    people:str
    checkin:str
    checkout:str

class insert_booking(BaseModel):
    
    numroom:int

class insert_addon(BaseModel):
    servicetype:str
    nameservice:str
    # price:int

class insert_debit(BaseModel):
    numcard:int
    cvv:int
    coupon:str

class insert_formaddhotel(BaseModel):
    hotelname: str
    rating: str
    numsroom: int
    hotelpicture: str
    location: str
    province: str

class insert_formaddroom(BaseModel):
    namehotel: str
    numroom: int
    types: str
    numpeople: int
    priceroom: int
    facs: str
    bedtype: str
    roompicture: str
    statusroom: bool    

class insert_formaddaddon(BaseModel):
    Typeservice:str
    Nameservice:str
    detail:str
    picture:str
    price:int
    namehotel:str
