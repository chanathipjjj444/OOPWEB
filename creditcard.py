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

