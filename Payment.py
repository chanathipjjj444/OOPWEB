class Payment:
    def __init__(self, total, transaction_id, payment_method, card_number, card_name, card_expire, cvv_card, vat):
        self.__total=total
        self.__transaction_id = transaction_id
        self.__payment_method = payment_method
        self.__card_number = card_number
        self.__card_name = card_name
        self.__card_expire = card_expire
        self.__cvv_card = cvv_card
        self.__vat = vat
    def payment_perform(self):
        pass
    def get_payment_status(self):
        pass
class Promotion:
    def __init__(self, typecoupon, discountnumroom):
        self.__total_coupon= typecoupon #list of Typecoupon
        self.__total_discount_num_room_list = discountnumroom #list of discountnumroo 

class TypeCoupon:
    def __init__(self, value_coupon, pr, coupon_description):
        self.__value_coupon = value_coupon
        self.__pr=pr
        self.__coupon_description=coupon_description

class DiscountNumRoom:
    def __init__(self, num_room_discount, value_discount):
        self.__num_room_discount = num_room_discount
        self.__value_discount = value_discount