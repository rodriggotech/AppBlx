from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from src.schemes.schemes import Produto
from src.schemes.schemes import Usuario
from src.infra.sqlalchemy.config.database import get_db, criar_db
from src.repositorios.produto import RepositorioProduto
from src.repositorios.usuario import RepositorioUsuario

criar_db()

app = FastAPI()

@app.post('/produtos')
def criar_produto(produto: Produto, db: Session = Depends(get_db)):
    produtos_criado = RepositorioProduto(db).criar(produto)
    return produtos_criado 

@app.get('/produtos')
def listar_produtos(db: Session = Depends(get_db)):
    produto = RepositorioProduto(db).listar()
    return produto

#rota nova por conta do repositorio usuario
@app.post('/usuarios')
def criar_usuario(usuario: Usuario, db: Session = Depends(get_db)):
    usuario_criado = RepositorioProduto(db).criar(usuario)
    return usuario_criado

@app.get('/usuarios')
def listar_usuarios(db: Session = Depends(get_db)):
    usuario = RepositorioUsuario(db).listar()

