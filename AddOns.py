class Addons:
    def __init__(self):
        self.add_on_list  =[]

    def add_breakfast_service(self, breakfast):
        breakfast_list=(breakfast.type_service, breakfast.detail ,breakfast.type_food, breakfast.price_food)
        self.add_on_list.append(breakfast_list)

    def add_spa_service(self, spa):
        spa_list=(spa.type_service, spa.detail, spa.spa_picture, spa.price_spa)
        self.add_on_list.append(spa_list)
    
    def get_add_on_list(self):
        return self.add_on_list

class BreakfastService():
    def __init__(self, type_service, detail, type_food, price_food):
        self.type_service = type_service
        self.detail = detail
        self.type_food = type_food
        self.price_food = price_food

class SpaService:
    def __init__(self, type_service, detail, spa_picture, price_spa):
        self.type_service = type_service
        self.detail = detail
        self.spa_picture = spa_picture
        self.price_spa = price_spa

class ActivityService:
    def __init__(self, type_service, detail, date_activity, num_person, price_activity):
        self.type_service = type_service
        self.detail = detail
        self.data_activity = date_activity
        self.num_person = num_person
        self.price_activity = price_activity

class TaxiService:
    def __init__(self, type_service, detail,number_taxi, fees_taxi, contact_taxi):
        self.type_service = type_service
        self.detail = detail
        self.number_taxi = number_taxi
        self.fees_taxi = fees_taxi
        self.contact_taxi = contact_taxi
