from datetime import datetime
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from workoutapi.contrib.models import BaseModel

class CentroDeTreinamentoModel(BaseModel):
    __tablename__ = 'centros_de_treinamento'

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(40), unique=True, nullable=False)
    endereco: Mapped[str] = mapped_column(String(60), nullable=False)
    proprietario: Mapped[str] = mapped_column(String(30), nullable=False)
    atleta: Mapped['AtletaModel'] = relationship(back_populates='centros_de_treinamento')