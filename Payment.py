from fastapi import FastAPI
from typing import List
from pydantic import BaseModel
from creditcard import Allcreditcard

class Promotion:
    def __init__(self):
        self.total_coupon= [] #list of Typecoupon
        self.total_discount_num_room_list = [] #list of discountnumroom

    def add_coupon(self, coupon):
        self.total_coupon.append(coupon)

    def get_coupon_list(self):
        return self.total_coupon

class Payment():
    def __init__(self, transaction_id : int):
        self.transaction_id = transaction_id
        self.money = 0
        self.price_room = 0
        self.status_payment = False
        self.total_day = 0
        self.total_price = 0
        self.add_on_price = 0

    def set_price_room(self, price_room):
        if isinstance(price_room,int):
            self.price_room = price_room

    def set_money(self,balance : int):
        # receive monet from a creditcard function
        self.money += balance
    
    def get_price_room(self):
        return self.price_room

    def get_payment_status(self):
        return self.status_payment
    
    def set_total_day(self, difference):
        self.total_day += difference
        print("Total day:",self.total_day)

    def set_add_on_price(self, add_on_price):
        self.add_on_price = add_on_price
        print("Add on price:",self.add_on_price)

    def set_total_price(self):
        self.total_price = (self.price_room * self.total_day) + self.add_on_price
        return {"Total price:": self.total_price}

    def use_coupon(self, promotion : Promotion):
        print("Do you want to use coupon:")
        requirement = input("True or False:")
        if requirement == "True":
            name_coupon = input("Enter coupon code:")
            for coupon in promotion.total_coupon:
                if coupon.name_coupon == name_coupon:
                    print("pre total price:",self.total_price)
                    self.total_price  -= coupon.value_coupon
                    print("post total price:",self.total_price)
                    break
            else:
                return {"Error":"Not found coupon code"}
        else:
            return {"Announcement":"Not used coupon code"}

    def process_payment(self):
        print("Process Payment...........")
        print("......")
        print("...")
        if(self.money >= self.total_price): #price_room must multiply day checkout-checkin
            print("Success Payment!!")
            self.money -= self.total_price
            print(self.money)
            self.status_payment = True
            return {"Success":f"Your balabce is {self.money}"}
        else:
            return {"Error":"Not enough money"}

class PaymentModel(BaseModel):
    money: int
    price_room: int
    status_payment: bool
    total_day: int
    total_price: int
    add_on_price: int
class TypeCoupon(BaseModel):
    name_coupon: str
    coupon_description: str
    value_coupon: int

class DiscountNumRoom(BaseModel):
    num_room_discount: int
    value_discount: int


app = FastAPI()
promotion = Promotion()
payment1 = Payment(1)
all_creditcard = Allcreditcard()


@app.post("/calculate")
def payment_perform(paymentModel : PaymentModel, transaction_id: int):
    payment = Payment(transaction_id)
    payment.set_money(paymentModel.money)
    payment.set_price_room(paymentModel.price_room)
    payment.set_total_day(paymentModel.total_day)
    payment.set_add_on_price(paymentModel.add_on_price)
    payment.set_total_price()
    payment.use_coupon(promotion)
    return payment.process_payment()

@app.get("/get_payment_status")
def get_payment_status():
    return payment1.money

@app.post("/add_coupon")
def add_coupon(coupon : TypeCoupon):
    promotion.add_coupon(coupon)
    return promotion.get_coupon_list()

@app.get("/get_coupon_list")
def get_coupon_list():
    return promotion.get_coupon_list()

#todo
#1. add coupon
#2. make payment