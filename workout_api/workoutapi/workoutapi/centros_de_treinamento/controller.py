from uuid import uuid4
from fastapi import APIRouter, Body, HTTPException, status
from pydantic import UUID4
from sqlalchemy.future import select

from workoutapi.centros_de_treinamento.schemas import CentroDeTreinamentoIn, CentroDeTreinamentoOut
from workoutapi.centros_de_treinamento.models import CentroDeTreinamentoModel
from workoutapi.contrib.repository.dependencies import DatabaseDependency

router = APIRouter()

@router.post('/', summary='Adicionar novo centro de treinamento', status_code=status.HTTP_201_CREATED, response_model=CentroDeTreinamentoOut)
async def post(db_session: DatabaseDependency, centrodetreinamento_in: CentroDeTreinamentoIn = Body(...)) -> CentroDeTreinamentoOut:
    centrodetreinamento_out = CentroDeTreinamentoOut(id=uuid4(), **centrodetreinamento_in.model_dump())
    centrodetreinamento_model = CentroDeTreinamentoModel(**centrodetreinamento_out.model_dump())
    
    db_session.add(centrodetreinamento_model)
    await db_session.commit()

    return centrodetreinamento_out

@router.get('/', summary='Consultar todos os centros de treinmento', status_code=status.HTTP_200_OK, response_model=list[CentroDeTreinamentoOut])
async def query(db_session: DatabaseDependency) -> list[CentroDeTreinamentoOut]:
    centrosdetreinamento: list[CentroDeTreinamentoOut] = (await db_session.execute(select(CentroDeTreinamentoModel))).scalars().all()
    return centrosdetreinamento

@router.get('/{id}', summary='Consultar Centro de Treinamento por ID', status_code=status.HTTP_200_OK, response_model=CentroDeTreinamentoOut)
async def query(id:UUID4, db_session: DatabaseDependency) -> CentroDeTreinamentoOut:
    centrodetreinamento: CentroDeTreinamentoOut = (await db_session.execute(select(CentroDeTreinamentoModel).filter_by(id=id))).scalars().first()

    if not centrodetreinamento:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Centro de Treinamento não encontrado no ID {id}.')

    return centrodetreinamento
