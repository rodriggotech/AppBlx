from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from src.schemes.schemes import Produto
from src.infra.sqlalchemy.config.database import get_db, criar_db
from src.repositorios.produto import RepositorioProduto


app = FastAPI()


criar_db()

@app.post('/produtos')
def criar_produtos(produto: Produto, db: Session = Depends(get_db)):
    produto_criado = RepositorioProduto().criar(produto)
    return produto_criado 

@app.get('/produtos')
def listar_produtos():
    return f'Listagem de produtos'
