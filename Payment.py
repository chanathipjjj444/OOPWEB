from promotion import Promotion
from fastapi import FastAPI
from typing import List
from pydantic import BaseModel
from creditcard import Allcreditcard,CreditCardModel

class Payment():
    def __init__(self, transaction_id : int):
        self.transaction_id = transaction_id
        self.status_payment = False
        self.total_day = 0
        self.total_price = 0

    def set_booking_details(self, booking):
        self.total_day = booking.total_days
        self.total_price = booking.total_price
        return {"Total days":self.total_day,"Result":self.total_price}

     
    def process_payment(self, booking,card_number, card_cvv,all_credit_cards: Allcreditcard, promotion:Promotion):
        print("Process Payment...........")
        print("......")
        print("...")
        self.set_booking_details(booking)
        card_balance = all_credit_cards.check_card_from_user(card_number, card_cvv)
        if card_balance is None:
            return {"message": "Credit card not found"}

        if card_balance < self.total_price:
            return {"message": "Insufficient balance"}

        self.status_payment = True
        self.use_coupon(promotion)
        card_balance -= self.total_price #money in card
        all_credit_cards.update_card_balance(card_number,card_cvv,card_balance)
        return {"message": "Payment processed successfully", "new_balance": card_balance}
        
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
                    return self.total_price
            else:
                return {"Error":"Not found coupon code"}
        else:
            return {"Announcement":"Not used coupon code"}
        
