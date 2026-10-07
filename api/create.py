from fastapi import APIRouter

router = APIRouter(
    prefix="/subscriptions"
)

@router.post("/create")
async def create_subscription(): 

    """
    method to add / create a new subscription 

    ideally this would be a db write but we're doing local json only 
    """
    
    pass 

