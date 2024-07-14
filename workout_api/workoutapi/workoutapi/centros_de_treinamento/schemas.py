from typing import Annotated
from pydantic import Field, UUID4
from workoutapi.contrib.schemas import BaseSchema

class CentroDeTreinamentoIn(BaseSchema):
    nome: Annotated[str, Field(description='Nome do centro de treinamento', example='CT Chaos', max_length=30)]
    endereco: Annotated[str, Field(description='Endereço do centro de treinamento', example='Avenida das Gardênias, 349', max_length=60)]
    proprietario: Annotated[str, Field(description='Nome do proprietário do centro de treinamento', example='Heitor Marques', max_length=50)]

class CentroDeTreinamentoAtleta(BaseSchema):
    nome: Annotated[str, Field(description='Nome do centro de treinamento', example='CT Chaos', max_length=30)]

class CentroDeTreinamentoOut(CentroDeTreinamentoIn):
    id: Annotated[UUID4, Field(description='Identificador do centro de treinamento')]