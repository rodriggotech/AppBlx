from fastapi import FastAPI
from src.schemes.schemes import Produto
from src.infra.sqlalchemy.repositorios.produto import RepositorioProduto

app = FastAPI()

@app.post('/produtos')
def criar_produtos(produto: Produto):
    return f'Produto cadastrado'

@app.get('/produtos')
def listar_produtos():
    return f'Listagem de produtos'
