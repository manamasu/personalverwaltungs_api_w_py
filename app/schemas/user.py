from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    full_name: str
    email: EmailStr
    password: str
    position: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserRead(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    position: str
    is_active: bool
    is_admin: bool

    class Config:
        # Pydantic models can also be created from arbitrary class instances by reading the instance attributes
        # corresponding to the model field names.
        # One common application of this functionality is integration with object-relational mappings (ORMs)

        # Quelle: https://docs.pydantic.dev/latest/concepts/models/#arbitrary-class-instances
        from_attributes = True
