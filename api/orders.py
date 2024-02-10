from fastapi import APIRouter

router = APIRouter()


@router.get("/order")
async def hello():
    return {"welcome to the orders shop"}
