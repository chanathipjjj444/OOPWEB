from pydantic import BaseModel


class CreditCardModel(BaseModel):
    card_number: int
    card_name : str
    surname : str
    card_cvv : int
    card_balance: int 

class Allcreditcard:
    def __init__(self):
        self.__creditcard_list = []

    def add_card(self, card : CreditCardModel): #done
        self.__creditcard_list.append(card)

    def check_card_from_user(self, cardnumber : int, cvv : int):
        for i in self.__creditcard_list:
            if i.card_number == cardnumber and i.card_cvv == cvv:
                return i.card_balance
            

    def update_card_balance(self, card_number, card_cvv, new_balance):
        for creditcard in self.__creditcard_list:
            if creditcard.card_number == card_number and creditcard.card_cvv == card_cvv:
                creditcard.card_balance = new_balance
                break
    
    @property
    def get_creditcard_list(self):
        return self.__creditcard_list

    def show_creditcard(self):
        for creditcard in self.__creditcard_list:
            print("Card number:",creditcard.card_number,"Card name:","Card Surname:",creditcard.surname,creditcard.card_name,"CVV card:",creditcard.card_cvv,
                "Card balance:",creditcard.card_balance)
