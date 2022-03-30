from sqlalchemy import Column, Interger, String, Float, Boolean
from src.infra.sqlalchemy.config.database import Base

class Produto(Base):
    __tablename__ = 'produto'

    id = Column(Interger, primary_key=True, index=True)
    nome = Column(String)
    detalhes = Column(String)
    preco = Column(Float)
    disponivel = Column(Bolean)
    codigo = Column(Interger)
