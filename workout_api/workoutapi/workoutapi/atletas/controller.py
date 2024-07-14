from datetime import datetime
from uuid import uuid4
from fastapi import APIRouter, Body, HTTPException, status
from pydantic import UUID4
from sqlalchemy.future import select

from workoutapi.atletas.schemas import AtletaIn, AtletaOut, AtletaUpdate
from workoutapi.atletas.models import AtletaModel
from workoutapi.categorias.models import CategoriaModel
from workoutapi.centros_de_treinamento.models import CentroDeTreinamentoModel
from workoutapi.contrib.repository.dependencies import DatabaseDependency

router = APIRouter()

@router.post('/', summary='Adicionar nova atleta', status_code=status.HTTP_201_CREATED, response_model=AtletaOut)
async def post(db_session: DatabaseDependency, atleta_in: AtletaIn = Body(...)):

    categoria_name = nome=atleta_in.categoria.nome
    categoria = (await db_session.execute(select(CategoriaModel).filter_by(categoria_name).scalars().first()))

    centro_de_treinamento_name = nome=atleta_in.centro_de_treinamento.nome
    centro_de_treinamento = (await db_session.execute(select(CentroDeTreinamentoModel).filter_by(centro_de_treinamento_name).scalars().first()))

    if not categoria:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f'A categoria {categoria_name} não foi encontrada.')
    
    if not centro_de_treinamento:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f'O centro de treinamento {centro_de_treinamento_name} não foi encontrado.')
    
    try:
        atleta_out = AtletaOut(id=uuid4(), created_at=datetime.utcnow(), **atleta_in.model_dump())
        atleta_model = AtletaModel(**atleta_out.model_dump(exclude={'categoria', 'centro_de_treinamento'}))
        atleta_model.categoria_id = categoria.pk_id
        atleta_model.centro_de_treinamento_id = centro_de_treinamento.pk_id
        
        db_session.add(atleta_model)
        await db_session.commit()

    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f'Ocorreu um erro ao inserir os dados no banco.')
    return atleta_out

@router.get('/', summary='Consultar todos as atletas', status_code=status.HTTP_200_OK, response_model=list[AtletaOut])
async def query(db_session: DatabaseDependency) -> list[AtletaOut]:
    atletas: list[AtletaOut] = (await db_session.execute(select(AtletaModel))).scalars().all()
    return [AtletaOut.model_validate() for atleta in atletas]

@router.get('/{id}', summary='Consultar Atleta pela ID', status_code=status.HTTP_200_OK, response_model=AtletaOut)
async def query(id:UUID4, db_session: DatabaseDependency) -> AtletaOut:
    atleta: AtletaOut = (await db_session.execute(select(AtletaModel).filter_by(id=id))).scalars().first()

    if not atleta:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Atleta não encontrado no ID {id}.')

    return atleta

@router.patch('/{id}', summary='Editar Atleta pela ID', status_code=status.HTTP_200_OK, response_model=AtletaOut)
async def query(id:UUID4, db_session: DatabaseDependency, atleta_up: AtletaUpdate = Body(...)) -> AtletaOut:
    atleta: AtletaOut = (await db_session.execute(select(AtletaModel).filter_by(id=id))).scalars().first()

    if not atleta:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Atleta não encontrado no ID {id}.')
    
    atleta_update = atleta.model_dump(exclude_unset=True)
    for key, value in atleta_update.items():
        setattr(atleta, key, value)

    await db_session.commit()
    await db_session.refresh(atleta)
    return atleta

@router.delete('/{id}', summary='Deletar Atleta pela ID', status_code=status.HTTP_204_NO_CONTENT)
async def query(id:UUID4, db_session: DatabaseDependency) -> None:
    atleta: AtletaOut = (await db_session.execute(select(AtletaModel).filter_by(id=id))).scalars().first()

    if not atleta:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Atleta não encontrado no ID {id}.')
    
    atleta_update = atleta.model_dump(exclude_unset=True)
    for key, value in atleta_update.items():
        setattr(atleta, key, value)

    await db_session.delete(atleta)
    await db_session.refresh()