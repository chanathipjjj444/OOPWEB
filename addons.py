class Addons:
    def __init__(self):
        self.add_on_list  =[]
        self.add_on_price = 0

    def add_service(self, service):
        service_list = (service.type_service,service.name_service,service.detail,service.picture,service.price_service)
        self.add_on_list.append(service_list)
    
    def get_add_on_list(self):
        print(self.add_on_list)
        
   
    def set_add_on_price(self, type_service, name_service):
        for add_on in self.add_on_list:
            if type_service == add_on[0] and name_service == add_on[1]:
                self.add_on_price = add_on[4]
                #print(self.__add_on_price)
                return self.add_on_price
        else:
            print(self.add_on_price)
        

class Service:
    def __init__(self,type_service,name_service,detail,picture,price_service):
        self.__type_service = type_service
        self.__name_service = name_service
        self.__detail = detail
        self.__picture = picture
        self.__price_service = price_service
    @property
    def type_service(self):
        return self.__type_service
    @property
    def name_service(self):
        return self.__name_service
    @property
    def detail(self):
        return self.__detail
    @property
    def picture(self):
        return self.__picture
    @property 
    def price_service(self):
        return self.__price_service    

add_on_cat = Addons()

breakfast1 = Service("breakfast","corn soup","Enjoy","soup",100)
add_on_cat.add_service(breakfast1)
spa1 = Service("spa","sisler salad","Enjoy","salad",120)
add_on_cat.add_service(spa1)
breakfast2 = Service("breakfast","chicken burger","Enjoy","chicken",100)
add_on_cat.add_service(breakfast2)