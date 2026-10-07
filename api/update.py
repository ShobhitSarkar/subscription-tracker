from fastapi import APIRouter

router = APIRouter(
    prefix="/subscriptions"
)

@router.post("/update")
async def update_subscription(): 

    """
    method to update a subscription 
    """
    
    pass 

