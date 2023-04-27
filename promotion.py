from pydantic import BaseModel

class TypeCoupon(BaseModel):
    name_coupon: str
    coupon_description: str
    value_coupon: int


class Promotion:
    def __init__(self):
        self.total_coupon= [] #list of Typecoupon

    def add_coupon(self, coupon:TypeCoupon):
        self.total_coupon.append(coupon)

    def get_coupon_list(self):
        return self.total_coupon
