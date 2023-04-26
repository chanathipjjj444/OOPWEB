# from Account import *
# from addons import *
from creditcard import *
from Payment import *
# from room import *
from hotel import *
import json
import requests
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

TEMPLATE = Jinja2Templates("html")

app = FastAPI()
all_creditcard = Allcreditcard()
promotion = Promotion()
payment = Payment(1)
#Hotel api 
catalog = HotelCatalog()

#creditcard api
allcreditcard = Allcreditcard()

catalog.add_hotel(HotelToAdd(name_hotel="Hotel A",rating = 4, num_rooms=100, hotel_picture="picture", location="Thailand", province="Bangkok", room_list=["room1","room2"], add_on_hotel="add_on"))
catalog.add_hotel(HotelToAdd(name_hotel="Hotel B",rating = 3, num_rooms=100, hotel_picture="picture", location="Thailand", province="Chonburi", room_list=["room1","room2"], add_on_hotel="add_on"))
catalog.add_hotel(HotelToAdd(name_hotel="Hotel C",rating = 5, num_rooms=100, hotel_picture="picture", location="Thailand", province="Chiangmai", room_list=["room1","room2"], add_on_hotel="add_on"))
catalog.add_hotel(HotelToAdd(name_hotel="Hotel D",rating = 2, num_rooms=100, hotel_picture="picture", location="Thailand", province="Phuket", room_list=["room1","room2"], add_on_hotel="add_on"))
catalog.add_hotel(HotelToAdd(name_hotel="Hotel E",rating = 1, num_rooms=100, hotel_picture="picture", location="Thailand", province="Pattaya", room_list=["room1","room2"], add_on_hotel="add_on"))


################################PAYMENT API#####################################

# @app.post("/calculates")
# async def payment_perform(paymentModel : PaymentModel, transaction_id : int):
#     payment.transaction_id = transaction_id
#     await payment.set_money(paymentModel.money)
#     await payment.set_price_room(paymentModel.price_room)
#     await payment.set_total_day(paymentModel.total_day)
#     await payment.set_add_on_price(paymentModel.add_on_price)
#     await payment.set_total_price()
#     await payment.use_coupon(promotion)
#     return await payment.process_payment()

@app.get("/get_payment_status")
async def get_payment_status():
    return payment.money

@app.post("/add_coupon")
async def add_coupon(coupon : TypeCoupon):
    promotion.add_coupon(coupon)
    return promotion.get_coupon_list()

@app.get("/get_coupon_list")
def get_coupon_list():
    return promotion.get_coupon_list()

###################################################################################
##################################HOTEL API########################################

@app.get("/hotels")
async def show_hotel():
    return catalog.hotel_list

@app.get("/hotels/{name}")
async def show_hotel1(name: str):
    return catalog.find_hotel(name)


@app.post("/hotels")
def add_hotel(hotel: HotelToAdd):
    catalog.add_hotel(hotel)
    return {"message": "Hotel added successfully"}

@app.get("/hotels/{name}")
def show_add_on(name: str):
    return catalog.show_add_on(name)

#####################################################################################

##################################CREDITCARD API#####################################

@app.post("/addcard")
def add_card(creditcard: CreditCardModel):
    allcreditcard.add_card(creditcard)
    allcreditcard.manage_card()
    return {"Success": f"{allcreditcard.card_number_list}",
            "Success2": f"{allcreditcard.card_name_list}",
            "Success3": f"{allcreditcard.cvv_card_list}"}

@app.get("/getbalance")
def get_balance(card_number: int):
    return allcreditcard.get_balance(card_number)

@app.get("/getcardnumber")
def get_card_number():
    return allcreditcard.card_number_list

@app.get("/getcardname")
def get_card_name():
    return allcreditcard.card_name_list

@app.get("/getcvvcard")
def get_cvv_card():
    return allcreditcard.cvv_card_list

######################################################################################

@app.get("/pre",response_class=HTMLResponse)
async def webLogin(request: Request):
    page_data = {"request": request}
    return TEMPLATE.TemplateResponse("index.html", page_data)


@app.get("/addcard", response_class=HTMLResponse)
async def addcard(request: Request):
    page_data = {"request": request}
    return TEMPLATE.TemplateResponse("add_creditcard.html", page_data)

@app.get("/addcoupon", response_class=HTMLResponse)
async def addcoupon(request: Request):
    page_data = {"request": request}
    return TEMPLATE.TemplateResponse("add_coupon.html", page_data)

###################################################

@app.get("/calculate",response_class=HTMLResponse)
async def check(request: Request):
    request_ = request.query_params
    balance = get_creditcard_balance(int(request_["cardnumber"]),int(request_["card_cvv"]))
    print(balance)
    await payment.set_money(balance)
    await payment.set_price_room(int(request_["price_room"]))
    await payment.set_total_day(int(request_["total_day"]))
    await payment.set_add_on_price(int(request_["add_on_price"]))
    await payment.set_total_price()
    await payment.use_coupon(promotion)
    a = await payment.process_payment()
    page_data = {"request": request, "addon_price": payment.add_on_pricetotal_price,"total_day":payment.total_day,"balance":a}
    return TEMPLATE.TemplateResponse("report.html", page_data)
    

#add creditcard with the CrediCardModel
@app.get("/add_creditcard", response_class=HTMLResponse)
async def add_creditcard(request: Request):
    request = request.query_params
    all_creditcard.add_card(CreditCardModel(card_number=int(request["card_number"]), card_cvv=int(request["card_cvv"]),name=request["name"],surname=request["surname"],card_balance=int(request["card_balance"])))
    print(all_creditcard.creditcard_list)
    return TEMPLATE.TemplateResponse("add_creditcard.html", {"request": request})


@app.get("/add_couponreal", response_class=HTMLResponse)
async def add_couponreal(request: Request, name_coupon, coupon_description, value_coupon):
    coupon = TypeCoupon(name_coupon=name_coupon,coupon_description=coupon_description,value_coupon=value_coupon)
    promotion.add_coupon(coupon)
    print(promotion.total_coupon)
    page_data = {"request": request}
    return TEMPLATE.TemplateResponse("add_coupon.html", page_data)

#check the card to get the balance 

@app.get("/get_balance/{card_number}/{card_cvv}")
def get_creditcard_list(card_number, card_cvv):
    r = requests.get(f'http://localhost:8000/get_creditcard?card_number={card_number}&card_cvv={card_cvv}')
    print(r)
    return r
    

def get_creditcard_balance(card_number:int, card_cvv:int):
    for card in all_creditcard.creditcard_list:
        if card.card_number == card_number and card.card_cvv == card_cvv:
            print(all_creditcard.creditcard_list[all_creditcard.creditcard_list.index(card)].card_balance)
            return all_creditcard.creditcard_list[all_creditcard.creditcard_list.index(card)].card_balance
    print("Card cvv or card number is incorrect")
    return {"message": "Card cvv or card number is incorrect"}

