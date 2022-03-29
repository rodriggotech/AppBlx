from pydantic import BaseModel
from typing import Optional, List


class Clientes(BaseModel):
    id: Optional[str] = None
    nome: str
    telefone: str
    meus_produtos: List[Produtos]
    minhas_vendas: List[Pedidos]
    meus_pedidos: List[Pedidos]

class Produtos(BaseModel):
    id: Optional[str] = None
    nome: str
    usuario: Usuario
    detalhes: str
    valor: float
    codigo: int
    disponivel: bool = False

class Pedidos(BaseModel):
    id: Optional[str] = None
    usuario: Usuario
    produto:Produtos 
    quantidade: int
    entrega: bool = True
    endereco: str
    observacos: Optional[str] = None




