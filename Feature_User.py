class Person:
    def __init__(self, prefix, name, surname, email, phone_number):
        self.__prefix = prefix
        self.__name = name
        self.__surname = surname
        self.__email = email
        self.__phone_number = phone_number
    def insert_person_info()
        pass
class Customer(Person):
    def __init__(self, prefix, name, surname, email, phone_number, creditcard_info,id,password):
        Person.__init__(self, prefix, name, surname, email, phone_number)
        self.id = id
        self.password = password
        self.__creditcard_info = creditcard_info

    def insert_creditcard_info()
        pass

class Booking:
    def __init__(self, check_in, check_out, price, location, country, creditcard_info):
        self.__check_in = check_in
        self.__check_out = check_out
        self.__price = price
        self.__location = location
        self.__country = country
        self.__creditcard_info = creditcard_info

    def create_booking()'
        pass