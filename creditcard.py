from fastapi import FastAPI
from typing import List
from pydantic import BaseModel


class CreditCardModel(BaseModel):
    card_number: int
    name : str
    card_cvv : int
    card_balance: int | None = None
    surname : str

class Allcreditcard:
    def __init__(self):
        self.creditcard_list = []


        # self.card_number_list =[]
        # self.card_name_list=[]
        # self.cvv_card_list=[]
        # self.balance_list =[]

    # def manage_card(self): #done
    #     for i in self.creditcard_list:
    #         if type(i) is CreditCardModel:
    #             self.card_number_list.append(i.card_number)
    #             self.card_name_list.append(i.card_name)
    #             self.cvv_card_list.append(i.card_cvv)
    #             self.balance_list.append(i.card_balance)
    #             self.creditcard_list.pop(self.creditcard_list.index(i))

    def add_card(self, card : CreditCardModel): #done
        self.creditcard_list.append(card)

    def check_card_from_user(self, cardnumber : int, cvv : int):
        for i in self.creditcard_list:
            if i.card_number == cardnumber and i.card_cvv == cvv:
                return i.card_balance

class Creditcard():
    def __init__(self, card_number, card_name, cvv_card):
        self.card_number = card_number
        self.card_name = card_name
        self.cvv_card = cvv_card
        self.balance = 0
        self.check_status_access = False
        self.check_end = 0

    def get_card_number(self):
        return self.card_number

    def get_card_name(self):
        return self.card_name
    
    def get_cvv_card(self):
        return self.cvv_card

    # def get_balance_in_card(self):
    #     return self.balance

    def get_allcard(self):
        return self.card_number_list

    def receive_data_card(self, creditcard : CreditCardModel):
        self.card_number = creditcard.card_number
        self.card_name = creditcard.card_name
        self.cvv_card = creditcard.card_cvv

    def get_balance(self, allcreditcard : Allcreditcard):# get the balamce from the allcreditcard_list to interact with the payment
        #get balance from card number
        for i in allcreditcard.card_number_list:
            if i == self.card_number:
                return allcreditcard.balance_list[allcreditcard.card_number_list.index(i)]
        return {"Error": "Card number not found"}



