import uuid
import json
from fastapi import APIRouter
from ..shapes import Subsctiption, DatabaseRecord

router = APIRouter(
    prefix="/subscriptions"
)

@router.post("/create")
async def create_subscription(sub: Subsctiption): 

    """
    method to add / create a new subscription 

    ideally this would be a db write but we're doing local json only 
    """

    uuid = uuid.uuid4()

    sub_record = DatabaseRecord(
        id = uuid, 
        Subsctiption = sub
    )

    try: 
        json_str = json.dumps(sub_record, indent=4)
        with open("../db.json", "w") as f:
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

