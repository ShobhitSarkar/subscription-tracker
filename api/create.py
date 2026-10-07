import uuid
import json
from fastapi import APIRouter
from shapes.shape import Subscription, DatabaseRecord

DB_PATH = "./db.json"

router = APIRouter(
    prefix="/subscriptions"
)

@router.post("/create")
async def create_subscription(sub: Subscription): 

    """
    method to add / create a new subscription 

    ideally this would be a db write but we're doing local json only 
    """

    key = uuid.uuid4()

    sub_record = DatabaseRecord(
        id = key, 
        subscription= sub
    )

    ## TODO: this currently just overwrites the file - need to change to append instead 
    
    try: 
        json_str = json.dumps(sub_record.model_dump(mode="json"), indent=4)
        with open(DB_PATH, "w") as f:
            f.write(json_str)
    except Exception as e: 
        return {
            "success": False, 
            "subscription": None 
        }
        
    return {
        "success": True,
        "subscription": sub_record 
    }

