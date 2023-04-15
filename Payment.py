from room import Booking

class Promotion:
    def __init__(self):
        self.total_coupon= [] #list of Typecoupon
        self.total_discount_num_room_list = [] #list of discountnumroom

    def add_coupon(self, coupon):
        self.total_coupon.append(coupon)

    def show_coupon_list(self):
        for discount in self.total_coupon:
            print("Total Coupon:",self.total_coupon)
    
    def get_coupon_list(self):
        return self.total_coupon

class Payment:
    def __init__(self, transaction_id, payment_method):
        self.__transaction_id = transaction_id
        self.__payment_method = payment_method
        self.__money = 0 
        self.__price_room = 0
        self.__status_payment =False
        self.__used_coupons = []
        self.__total_day = 0
        self.__total_price = 0
        self.__add_on_price = 0
    
    def set_price_room(self, price_room):
        if isinstance(price_room,int):
            self.__price_room = price_room
    
    def set_money(self,balance):
        self.__money += balance
    
    def get_price_room(self):
        return self.__price_room
    
    def payment_perform(self):
        pass
    
    def get_payment_status(self):
        return self.__status_payment
    
    def set_total_day(self, difference):
        self.__total_day += difference
        print("Total day:",self.__total_day)

    def set_add_on_price(self, add_on_price, book1=Booking):
        self.__add_on_price = book1.service_price
        print("Add on price:",self.__add_on_price)

    def set_total_price(self):
        self.__total_price = (self.__price_room * self.__total_day) + self.__add_on_price
        print("Total price:",self.__total_price)

    def use_coupon(self, promotion : Promotion):
        print("Do you want to use coupon:")
        requirement = input("True or False:")
        if requirement == "True":
            name_coupon = input("Enter coupon code:")
            for coupon in promotion.total_coupon:
                if coupon.name_coupon == name_coupon:
                    self.__total_price  -= coupon.value_coupon
                    break
            else:
                print("Invalid coupon name")
        else: 
            print("Not use coupon")

    def process_payment(self):
        print("Process Payment...........")
        print("......")
        print("...")
        if(self.__money >= self.__total_price): #price_room must multiply day checkout-checkin

            if self.use_coupon:
                print("Total after use coupon code:",self.__total_price)
            
            print("Success Payment!!")
            self.__money-=self.__total_price
            self.__status_payment = True
            print("Payment status is True")
            print("Your Balance is",self.__money)
            return True
        else:
            print("Fail Payment")
            return False



class TypeCoupon:
    def __init__(self, name_coupon, coupon_description, value_coupon):
        self.name_coupon = name_coupon
        self.coupon_description=coupon_description
        self.value_coupon = value_coupon
class DiscountNumRoom:
    def __init__(self, num_room_discount, value_discount):
        self.num_room_discount = num_room_discount
        self.value_discount = value_discount
