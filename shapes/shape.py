from pydantic import BaseModel, Enum

class Subscription(BaseModel): 
    """
    shape of the notifications object 
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
    