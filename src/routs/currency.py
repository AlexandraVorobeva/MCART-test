from fastapi import APIRouter


router = APIRouter(prefix="/currency")


@router.get('/all')
def get_list_of_currencies():
    pass



@router.get('/difference')
def get_rub_difference():
    pass