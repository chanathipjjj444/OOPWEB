class Addons:
    def __init__(self):
        self.add_on_list  =[]
        self.add_on_price = 0

    def add_breakfast_service(self, breakfast):
        breakfast_list=(breakfast.type_service, breakfast.detail ,breakfast.food_picture, breakfast.price_food)
        self.add_on_list.append(breakfast_list)

    def add_spa_service(self, spa):
        spa_list=(spa.type_service, spa.detail, spa.spa_picture, spa.price_spa)
        self.add_on_list.append(spa_list)
    
    def get_add_on_list(self):
        print(self.add_on_list)
        

    def set_add_on_price(self, type_service, detail):
        for add_on in self.add_on_list:
            if type_service == add_on[0] and detail == add_on[1]:
                self.add_on_price = add_on[3]
                #print(self.add_on_price)
                return self.add_on_price
        else:
            print(self.add_on_price)
        


class BreakfastService():
    def __init__(self, detail, food_picture, price_food):
        self.type_service = "breakfast"
        self.detail = detail
        self.food_picture = food_picture
        self.price_food = price_food

class SpaService:
    def __init__(self,detail, spa_picture, price_spa):
        self.type_service = "spa"
        self.detail = detail
        self.spa_picture = spa_picture
        self.price_spa = price_spa


class ActivityService:
    def __init__(self,detail, date_activity, num_person, price_activity):
        self.type_service = "activity"
        self.detail = detail
        self.data_activity = date_activity
        self.num_person = num_person
        self.price_activity = price_activity

class TaxiService:
    def __init__(self,detail,number_taxi, fees_taxi, contact_taxi):
        self.type_service = "taxi"
        self.detail = detail
        self.number_taxi = number_taxi
        self.fees_taxi = fees_taxi
        self.contact_taxi = contact_taxi

add_on_cat = Addons()
breakfast1 = BreakfastService("corn soup","soup", 200)
breakfast2 = BreakfastService("sisler salad","salad",120)
spa1 = SpaService("hand spa","picture",500)
add_on_cat.add_breakfast_service(breakfast1)
add_on_cat.add_spa_service(spa1)
add_on_cat.add_breakfast_service(breakfast2)

add_on_cat.get_add_on_list()
add_on_cat.set_add_on_price("breakfast","corn soup")
