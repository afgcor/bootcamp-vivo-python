from fastapi import APIRouter
from workoutapi.atletas.controller import router as atletas
from workoutapi.categorias.controller import router as categorias
from workoutapi.centros_de_treinamento.controller import router as centros_de_treinamento

api_router = APIRouter()
api_router.include_router(atletas, prefix='/atletas', tags=['atletas'])
api_router.include_router(categorias, prefix='/categorias', tags=['categorias'])
api_router.include_router(centros_de_treinamento, prefix='/centros_de_treinamento', tags=['centros_de_treinamento'])