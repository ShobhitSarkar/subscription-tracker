from fastapi import APIRouter

router = APIRouter(
    prefix="/subscriptions"
)

@router.post("/delete/{id}")
async def delete_subscription(id: int): 

    """
    method to delete a particular subscription
    """
    
    pass 

