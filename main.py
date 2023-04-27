from fastapi import FastAPI,status
from starlette.middleware.cors import CORSMiddleware
from fastapi import Request,HTTPException,Depends
from fastapi import responses
from fastapi import status

from model import (insert_register,
   insert_login)



app = FastAPI()

origins =[
    'http://localhost:3000',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

# @app.get("/")
# async def root():
#    return {"hello goodbye"} 



class Profile:
    def __init__(self, prefix, name, surname, email, phone_number):
        self._prefix = prefix
        self._name = name
        self._surname = surname
        self._email = email
        self._phone_number = phone_number

class User:
    def __init__(self,data_user):
        self.data_set = {}
        self.data_set.update(data_user)
        self.__data_user = list(self.data_set.values())
        self.__name = self.__data_user[0]
        self.__email = self.__data_user[1]
        self.__password = self.__data_user[2]
        self.__phone = self.__data_user[3]
        self.__address = self.__data_user[4]

    @property
    def name(self):
        return self.__name
    
    @property
    def email(self):
        return self.__email
    
    @property
    def password(self):
        return self.__password
    
    @property
    def phone(self):
        return self.__phone
    
    @property
    def address(self):
        return self.__address   


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

class Collectuser:
    collect = []

class Register:
    def __init__(self) -> None:
        self.__user_dict ={}

    def update(self, data, collect):
        # self.__user_dict.update(data)
        # collect.append(self.__user_dict)
        if(self.check_update(data,collect)):
            collect.append(data)
            print(self.__user_dict)
            return  self.__user_dict
        print(self.__user_dict)
        return  self.__user_dict
    
    def check_update(self,data,collect):
        for check in collect:
            if check.email == data.email or check.password == data.password:
                print("invalid register")
                return 0
        print("Success register")
        return 1
        
class Login:
    def __init__(self, data):
        self.__data_set = {}
        self.__data_set.update(data)
        self.__data_list = list(self.__data_set.values())
        self.__user_email = self.__data_list[0]
        self.__user_password = self.__data_list[1]
        self.__user_name = ""
    
    def check_login(self, data_collect):
        for check in data_collect:
            if check.email == self.__user_email and check.password == self.__user_password:
                print("Success login!!")
                self.__user_name = check.name
                return self.show_detail()
        print("invalid login")
        return {}
        
    def show_detail(self):
        view_account = {
            "name" : self.__user_name,
            "email" : self.__user_email
        }
        return view_account




@app.post("/register",response_model=insert_register)
async def register(Insert_register : insert_register):
   # user = User(Insert_register)
   # user.process_data()
   collect_user = Collectuser()
   user =User(Insert_register)
   register =Register()
   response = register.update(user, collect_user.collect)
   print(collect_user.collect)
   if response:
      return response
   else:
      raise HTTPException(status_code=400, detail="Something error")

   
@app.post("/login",response_model=insert_login,status_code=status.HTTP_200_OK)
async def login(Insert : insert_login):
      collect_user = Collectuser()
      login = Login(Insert)
      response = login.check_login(collect_user.collect)
      if response:
         return responses.JSONResponse(response)
          

   
