class Profile:
    def __init__(self, prefix, name, surname, email, phone_number):
        self._prefix = prefix
        self._name = name
        self._surname = surname
        self._email = email
        self._phone_number = phone_number

class User:
    def __init__(self, name, id, password):
        self._id = id
        self._password = password
        self._name = name
        self._user_list =[]
    def add_user(self, user):
        self._user_list.append(user)

class Admin:
    def __init__(self, name, id, password):
        self._id = id
        self._password = password
        self._name = name
        self._admin_list =[]
    def add_admin(self, admin):
        self._admin_list.append(admin)

class Login:
    def __init__(self, id, password):
        self._id = id
        self._password = password
        self.admin_list = []
        self.user_list = []
    def check_id(self, admin_list, user_list):
        self.admin_list = admin_list
        self.user_list = user_list
        for admin in self.admin_list:
            if self._id == admin._id and self._password == admin._password:
                return print("ซ้ำโว้ยยย")
            else:
                return print(admin._id, admin._password)
        for user in self.user_list:
            if self._id == user._id and self._password == user._password:
                return print("ซ้ำโว้ยยย")
            else:
                return print(user._id, user._password)


user = User("Tung","kiki123@gmail.com","12345678")
user.add_user(user)
admin = Admin("Tung","kiki123@gmail.com","1234567")
admin.add_admin(admin)

login = Login(user._id,user._password)
login.check_id(admin._admin_list,user._user_list)
# print(user._user_list)