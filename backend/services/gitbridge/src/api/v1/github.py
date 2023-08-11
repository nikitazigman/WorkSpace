from fastapi import APIRouter

router = APIRouter()


@router.post(path="/")
def test_endpoint():
    return {"message": "Hello World!"}
