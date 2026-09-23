from fastapi import APIRouter

from exercise_model import Muscolo, Attrezzo

from api_wrapper.schemas import InfoEsercizio
from api_wrapper.service import catalogo_esercizi

router = APIRouter(tags=["catalogo"])


@router.get("/muscoli", response_model=list[Muscolo])
def lista_muscoli():
    return list(Muscolo)

@router.get("/attrezzi", response_model=list[Attrezzo])
def lista_attrezzi():
    return list(Attrezzo)

@router.get("/esercizi", response_model=list[InfoEsercizio])
def lista_esercizi():
    return catalogo_esercizi()
