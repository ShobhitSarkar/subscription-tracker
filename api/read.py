from fastapi import APIRouter

router = APIRouter(
    prefix="/subscriptions"
)

@router.post("/readall")
async def get_all_subscriptions(): 

    """
    return all the subscriptions
    """
    
    pass 

@router.post("read/{id}")
async def return_subscription(id: int): 
    """
    return a particular subscription
    """
    pass 
