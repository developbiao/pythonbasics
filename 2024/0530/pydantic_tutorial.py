from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, ValidationError

class User(BaseModel):
    id: int
    name: str = 'John Doe'
    signup_ts: Optional[datetime] = None
    friends: List[int] = []

external_data = {'id': '123', 'signup_ts': '2023-06-01 12:22', 'friends': [1, '2', b'3']}
#user = User(**external_data)
user = User.parse_obj(external_data)
print(user)
#> User id=123 name='John Doe' signup_ts=datetime.datetime(2017, 6, 1, 12, 22) friends=[1, 2, 3]
print(user.id)
#> 123

print(repr(user.signup_ts))

print("\033[31m2. Validation error\033[0m")
try:
    User(id=3, signup_ts=datetime.today(), friends=[1, 2, 'not number'])
except ValidationError as e:
    print(e.json())
