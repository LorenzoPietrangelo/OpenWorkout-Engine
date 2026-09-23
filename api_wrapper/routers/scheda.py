from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from api_wrapper.schemas import RichiestaScheda, Scheda
from api_wrapper.service import scheda_json, scheda_csv

router = APIRouter(prefix="/scheda", tags=["scheda"])


@router.post("", response_model=Scheda)
def crea_scheda(richiesta: RichiestaScheda):
    return scheda_json(richiesta)

@router.post("/csv", response_class=StreamingResponse)
def crea_scheda_csv(richiesta: RichiestaScheda):
    return StreamingResponse(scheda_csv(richiesta), media_type="text/csv",
                             headers={"Content-Disposition": "attachment; filename=scheda.csv"})
