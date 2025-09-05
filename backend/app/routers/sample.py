from fastapi import APIRouter

router = APIRouter()

@router.get('/')
def read_items():
    return [{'id': 1, 'name': 'Sample item'}]
