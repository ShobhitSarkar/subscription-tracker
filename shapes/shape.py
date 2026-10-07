import uuid
from pydantic import BaseModel
from enum import Enum


class Subscription(BaseModel): 
    """
    shape of the notifications object (outwards facing)
    """
    name: str
    frequency: FrequenciesEnum
    cost: int


class FrequenciesEnum(str, Enum): 
    """
    frequency of the subsctiption
    """
    d = "daily"
    w = "weekly"
    m = "monthly"
    y = "yearly"

class DatabaseRecord(BaseModel): 
    """
    shape of the object that we write to the db
    """

    id: uuid.UUID
    subscription: Subscription