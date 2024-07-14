from typing import Annotated, Optional
from pydantic import Field, PositiveFloat

from workoutapi.contrib.schemas import BaseSchema, OutMixin
from workoutapi.categorias.schemas import CategoriaIn
from workoutapi.centros_de_treinamento.schemas import CentroDeTreinamentoIn

class Atleta(BaseSchema):
    nome: Annotated[str, Field(description='Nome do atleta', example='Rafaela', max_length=50)]
    cpf: Annotated[str, Field(description='CPF do atleta', example='11122233344', max_length=11)]
    idade: Annotated[int, Field(description='Idade do atleta', example=25)]
    peso: Annotated[PositiveFloat, Field(description='Peso do atleta', example=72.5)]
    altura: Annotated[PositiveFloat, Field(description='Altura do atleta', example=1.80)]
    sexo: Annotated[str, Field(description='Sexo do atleta', example='F', max_length=1)]
    categoria: Annotated[CategoriaIn, Field(description='Categoria do atleta')]
    centro_de_treinamento: Annotated[CentroDeTreinamentoIn, Field(description='Centro de treinamento do atleta')]

class AtletaIn(Atleta):
    pass

class AtletaOut(Atleta, OutMixin):
    pass

class AtletaUpdate(BaseSchema):
    nome: Annotated[Optional[str], Field(None, description='Nome do atleta', example='Rafaela', max_length=50)]
    idade: Annotated[Optional[int], Field(None, description='Idade do atleta', example=25)]
    peso: Annotated[Optional[PositiveFloat], Field(None, description='Peso do atleta', example=72.5)]
    altura: Annotated[Optional[PositiveFloat], Field(None, description='Altura do atleta', example=1.80)]
    categoria: Annotated[Optional[CategoriaIn], Field(None, description='Categoria do atleta')]
    centro_de_treinamento: Annotated[Optional[CentroDeTreinamentoIn], Field(None, description='Centro de treinamento do atleta')]