from sqlalchemy import Column, Integer, String, Float, Boolean
from src.infra.sqlalchemy.config.database import Base

class Produtos(Base): 
    __tablename__ = 'produto'
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    detalhes = Column(String)
    preco = Column(Float)
    codigo = Column(Integer)
    disponivel = Column(Boolean)