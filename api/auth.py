from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def hello():
    return {"welcome to the pizza shop"}
