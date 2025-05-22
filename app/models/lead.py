from pydantic import BaseModel
from typing import Optional

class Lead(BaseModel):
    id: Optional[int]
    email : str
    created_at: str


    @staticmethod
    def to_json(lead):
        return {
            "id": lead.id,
            "email": lead.email,
            "created_at": lead.created_at
        }
    
    @staticmethod
    def factory(lead):
        return Lead(
            id=lead[0],
            email=lead[1],
            created_at=lead[2]
        )
    
