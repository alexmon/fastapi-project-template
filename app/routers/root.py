from fastapi import APIRouter

router = APIRouter()

@router.get(
    "/",
    tags=["healthcheck"],
    summary='healthcheck'
)
def read_root():
    '''
    This route will serve as a healthcheck endpoint
    '''
    return {"status": "OK"}