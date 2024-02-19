from pydantic import BaseModel, EmailStr, validator

def get_full_name(names: list[str]):
    for name in names:
        print(name.capitalize())

class User(BaseModel):
    name: str
    email: EmailStr
    account_id: int
    
    @validator("account_id")
    def validate_account_id(cls, value):
        if value <= 0:
            return ValueError(f"account_id muste be positive: {value}")
        return value

def createUser():
    user_data = {
        'name': 'Jack',
        'email': 'jack@gmail.com',
        'account_id': 1234
    }
    user = User(**user_data)
    print(user)
    print(user.model_dump_json())

createUser()
 