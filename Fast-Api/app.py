from fastapi import FastAPI, HTTPException
#from typing import Union
from typing import List
#from pydantic import BaseModel
from models import User, Role
from uuid import UUID #,uuid4

app = FastAPI()

#class Item(BaseModel):
#    name: str
#    price: float
#    is_offer: Union[bool, None] = None

db: List[User] = [
    User(
        id=UUID("905958e7-ed7e-41d9-814b-d0729784470a"),
         first_name="Kassia", 
         last_name="Santo", 
         email="kassiaes@gmail.com", 
         role=[Role.role_1]
    ),    
    User(
        id=UUID("c4b57647-ddba-483e-9442-3a0de9c50832"),
         first_name="Paula", 
         last_name="Pirozzi", 
         email="paula@gmail.com", 
         role=[Role.role_2]
    ),
    User(
        id=UUID("0906ea78-14d7-406e-847a-552eb57f8456"),
         first_name="Amanda", 
         last_name="Pirozzi", 
         email="amanda@gmail.com", 
         role=[Role.role_3]
    )
]

@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}

@app.get("/api/users")
async def get_users():
    return db;

@app.get("/api/users/{id}")
async def get_user(id: UUID):
    for user in db:
        if user.id == id:
            return user
    raise HTTPException(status_code=404, detail="Usuário não encontrado!")

@app.post("/api/users")
async def add_user(user: User):
    db.append(user)
    return {"id": user.id}

@app.delete("/api/users/{id}")
async def del_user(id: UUID):
    for user in db:
        if user.id == id:
            db.remove(user)
            return
    raise HTTPException(
        status_code=404,
        detail=f"Usuário com o id{id} não encontrado!"
    )

@app.put("/api/users/{id}")
async def update_user(id: UUID, updated_user: User):
    for index, user in enumerate(db):
        if user.id == id:
            db[index] = updated_user
            return {"message": "Usuário atualizado com sucesso!"}
    raise HTTPException(
        status_code=404,
        detail=f"Usuário com o id {id} não encontrado!"
    )

#@app.get("/itens/{item_id}")
#async def read_item(item_id: int, busca: Union[str,int] = None):
#    return {"item_id": item_id, "busca": busca}

#@app.put("/itens/{item_id}")
#async def update_item(item_id: int, item: Item):
#    return {"item_name": item.name, "item_id": item_id}