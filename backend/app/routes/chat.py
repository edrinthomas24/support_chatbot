from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from ..services.chat_service import handle_query
from ..models.schemas import ChatRequest

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@router.post("/query")
async def chat_endpoint(request: ChatRequest, token: str = Depends(oauth2_scheme)):
    try:
        return await handle_query(request.question)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
