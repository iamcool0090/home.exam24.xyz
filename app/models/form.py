from pydantic import BaseModel, EmailStr, Field


class ContactForm(BaseModel):
    email: EmailStr = Field(..., description="Email address of the user")

