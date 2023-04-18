from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

app = FastAPI()

TEMPLATE = Jinja2Templates("html")
class Profile:
    def __init__(self, prefix, name, surname, email, phone_number):
        self._prefix = prefix
        self._name = name
        self._surname = surname
        self._email = email
        self._phone_number = phone_number

class User:
    def __init__(self, name, id, password):
        self.__id = id
        self.__password = password
        self.__name = name

    @property
    def name(self):
        return self.__name
    
    @property
    def id(self):
        return self.__id
    
    @property
    def password(self):
        return self.__password

class Admin:
    def __init__(self, name, id, password):
        self.__id = id
        self.__password = password
        self.__name = name

    @property
    def name(self):
        return self.__name
    
    @property
    def id(self):
        return self.__id
    
    @property
    def password(self):
        return self.__password
    
class Login:
    def __init__(self):
        self.__admin_list = []
        self.__user_list = []
    
    @property
    def user_list(self):
        return self.__user_list

    def add_user(self, user):
        self.__user_list.append(user)

    def add_admin(self, admin):
        self.__admin_list.append(admin)

    def check_id(self, account):
        for admin in self.__admin_list:
            if admin.id == account.id and admin.password == account.password:
                return print("ซ้ำโว้ยยย")
            else:
                return account
        for user in self.__user_list:
            if user.id == account.id and user.password == account.password:
                return print("ซ้ำโว้ยยย")
            else:
                return account

    def show_detail(self, account):
        view_account = {
            "name" : account.name,
            "email" : account.id,
            "password" : account.password
        }
        return view_account


user = User("Tung","kiki123@gmail.com","12345678")
admin = Admin("Tung","kiki123@gmail.com","1234567")

login = Login()
login.add_user(user)
login.add_admin(admin)
login.check_id(user)
login.check_id(admin)

@app.get("/create_account/{name}")
async def get_user(name:str):
    for detail in login.user_list:
        if  detail.name == name:
            return login.show_detail(detail)
        
@app.get("/list_account")
async def get_list():
    return {"list" : login.user_list}

@app.get("/login",response_class=HTMLResponse)
async def webLogin(request: Request):
    page_data = {"request": request}
    return TEMPLATE.TemplateResponse("login.html", page_data)

@app.get("/register",response_class=HTMLResponse)
async def WebRegister(request: Request):
    page_data = {"request": request}
    return TEMPLATE.TemplateResponse("register.html", page_data)

@app.get("/add_account",response_class=HTMLResponse)
async def check(request: Request, name, email, password):
    account = User(name, email, password)
    page_data = {"request": request}
    login.user_list.append(login.check_id(account))
    return TEMPLATE.TemplateResponse("register.html", page_data)


@app.post("/list_account")
async def add_account(name, id, password):
    account = User(name, id, password)
    login.user_list.append(account)
    return {"Data" : login.user_list}

# r = requests.get("http://127.0.0.1:8000/list_account")
# print(r.json())

# print(login.show_detail(user))