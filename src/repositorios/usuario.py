from sqlalchemy.orm import Session
from src.schemes import schemes
from src.infra.sqlalchemy.models import models

class RepositorioUsuario():
    def __init__(self, db: Session):
        self.db = db

    def criar(self, usuario:schemes.Usuario):
        db_usuario = models.Usuario(
            nome = usuario.nome,
            telefone = usuario.telefone
        )

        self.db.add(db_usuario)
        self.db.commit()
        self.db.refresh(db_usuario)
        return db_usuario

    def listar(self):
        usuario = self.db.query(models.Usuario).all()
        return usuario 

## se tiver dando erro so apagar aqui, ou verificar
