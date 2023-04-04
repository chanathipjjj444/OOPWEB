class Addons:
    def __init__(self):
        self.add_on_list  =[]
    '''    
    def get_addons(self, detail, all_services):
        addons = (all_services.__type_food)
        self.__detail = detail
        self.__add_on_list.append(addons)
    '''
    def add_breakfast_service(self, breakfast):
        breakfast_list=(breakfast.detail ,breakfast.type_food, breakfast.price_food)
        self.add_on_list.append(breakfast_list)
    
    def get_add_on_list(self):
        return self.add_on_list
    
class BreakfastService():
    def __init__(self, detail, type_food, price_food):
        self.detail = detail
        self.type_food = type_food
        self.price_food = price_food
    '''
    def get_detail(self):
        return self.detail
    def get_type_food(self):
        return self.type_food
    def get_price_food(self):
        return self.price_food
    '''
class SpaService:
    def __init__(self, detail,reserve_spa, price_service):
        self.detail = detail
        self.reserve_spa = reserve_spa
        self.price_service = price_service

class ActivityService:
    def __init__(self, detail, date_activity, price_activity, num_person):
        self.detail = detail
        self.data_activity = date_activity
        self.price_activity = price_activity
        self.num_person = num_person

class TaxiService:
    def __init__(self, detail,number_taxi, fees_taxi, contact_taxi):
        self.detail = detail
        self.number_taxi = number_taxi
        self.fees_taxi = fees_taxi
        self.contact_taxi = contact_taxi