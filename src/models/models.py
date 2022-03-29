from pydantic import BaseModel

class Clientes(BaseModel):
    id: str
    name: str
    telefone: str

