from pydantic import BaseModel, Field

class AddressBase(BaseModel):
    name: str
    street: str
    city: str
    latitude: float = Field(..., ge=-90, le=90, description="Latitude must be between -90 and 90")
    longitude: float = Field(..., ge=-180, le=180, description="Longitude must be between -180 and 180")

class AddressCreate(AddressBase):
    pass

class AddressUpdate(AddressBase):
    pass

class Address(AddressBase):
    id: int

    class Config:
        from_attributes = True  # Allows Pydantic to read data from SQLAlchemy models