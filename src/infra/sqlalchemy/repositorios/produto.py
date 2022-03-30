from slqalschemy.orm import Session
from src.schemes.schemes import schemes
from src.infra.sqlalchemy.models import models

class RepositorioProduto():
    def __init__(self, db: Session):
        self.db = db

    def criar(self, produto: schemes.Produto):
        db_produto = models.Produto(
            nome = produto.nome,
            detalhes = produto.detalhes,
            preco = produto.preco,
            disponivel = produto.disponivel,
            codigo = produto.codigo
        )

        self.db.add(db_produto)
        self.db.commit()
        self.db.refresh(db_produto)
        return db_produto 

    def listar(self):
        produtos = self.db.qurey(models.produto).all()
        return produtos

    def obter(self):
        pass

    def remover(self):
        pass
