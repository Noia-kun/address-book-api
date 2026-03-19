from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from .. import crud, schemas, database

router = APIRouter(
    prefix="/addresses",
    tags=["addresses"]
)

# 1. CREATE
@router.post("/", response_model=schemas.Address, status_code=status.HTTP_201_CREATED)
def create_address(address: schemas.AddressCreate, db: Session = Depends(database.get_db)):
    """Create a new entry in the address book."""
    return crud.create_address(db=db, address=address)

# 2. READ ALL (With Distance Search)
@router.get("/", response_model=List[schemas.Address])
def read_addresses(
    lat: float = None, 
    lon: float = None, 
    radius_km: float = None, 
    db: Session = Depends(database.get_db)
):
    """
    Retrieve addresses. 
    If lat, lon, and radius are provided, it filters by distance.
    Otherwise, it returns all addresses.
    """
    if lat is not None and lon is not None and radius_km is not None:
        return crud.get_addresses_within_range(db, lat, lon, radius_km)
    
    return crud.get_addresses(db)

# 3. READ ONE
@router.get("/{address_id}", response_model=schemas.Address)
def read_address(address_id: int, db: Session = Depends(database.get_db)):
    """Retrieve a specific address by its ID."""
    db_address = crud.get_address(db, address_id=address_id)
    if db_address is None:
        raise HTTPException(status_code=404, detail="Address not found")
    return db_address

# 4. UPDATE
@router.put("/{address_id}", response_model=schemas.Address)
def update_address(address_id: int, address: schemas.AddressUpdate, db: Session = Depends(database.get_db)):
    """Update an existing address."""
    db_address = crud.update_address(db, address_id=address_id, address_update=address)
    if db_address is None:
        raise HTTPException(status_code=404, detail="Address not found")
    return db_address

# 5. DELETE
@router.delete("/{address_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_address(address_id: int, db: Session = Depends(database.get_db)):
    """Delete an address from the database."""
    success = crud.delete_address(db, address_id=address_id)
    if not success:
        raise HTTPException(status_code=404, detail="Address not found")
    return None