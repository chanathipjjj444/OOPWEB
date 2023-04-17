# from Account import *
# from addons import *
from creditcard import *
from Payment import *
# from room import *
from hotel import *
from fastapi import FastAPI, APIRouter
from typing import List
from pydantic import BaseModel
import json
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


# router = APIRouter()
# router.include_router(user_router, prefix="/users",tags=["users"])
# router.include_router(article_router, prefix="/articles",tags=["articles"])
app = FastAPI()
# app.include_router(router)
all_creditcard = Allcreditcard()
promotion = Promotion()
payment1 = Payment(1)

#Hotel api 
catalog = HotelCatalog()

#creditcard api
allcreditcard = Allcreditcard()

coupon1 = TypeCoupon(name_coupon="AA",coupon_description="For AA discount",value_coupon=1000)
coupon2 = TypeCoupon(name_coupon="BB",coupon_description="For BB discount",value_coupon=1500)
coupon3 = TypeCoupon(name_coupon="CC",coupon_description="For CC discount",value_coupon=2000)

promotion.add_coupon(coupon1)
promotion.add_coupon(coupon2)
promotion.add_coupon(coupon3)

# print(promotion.get_coupon_list())


################################PAYMENT API#####################################

@app.post("/calculates")
async def payment_perform(paymentModel : PaymentModel, transaction_id: int):
    payment = Payment(transaction_id)
    payment.set_money(paymentModel.money)
    payment.set_price_room(paymentModel.price_room)
    payment.set_total_day(paymentModel.total_day)
    payment.set_add_on_price(paymentModel.add_on_price)
    payment.set_total_price()
    payment.use_coupon(promotion)
    return await payment.process_payment()

@app.get("/get_payment_status")
async def get_payment_status():
    return payment1.money

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

@app.get("/hotels/{name}/rooms")
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

@app.get("/getbalance")
def get_balance():
    return Creditcard.get_balance(allcreditcard)

@app.get("/getbalance")
def get_balance(card_number: int):
    return allcreditcard.get_balance(card_number)

#####################################################################################

@app.get("/")
def get_balance():
    return {"message": "Hello World"}

print(requests.get("http://https://api.coindesk.com/v1/bpi/currentprice.json", verify=False).json())
print(requests.get("http://https://api.coindesk.com/v1/bpi/currentprice.json", verify=False).json())
print("Hello World")