import logging
from sqlalchemy.orm import Session
from . import models, schemas
from .utils.geo import calculate_distance

# Set up logging for this file
logger = logging.getLogger(__name__)

def get_address(db: Session, address_id: int):
    """Retrieve a single address by ID."""
    return db.query(models.Address).filter(models.Address.id == address_id).first()

def get_addresses(db: Session, skip: int = 0, limit: int = 100):
    """Retrieve a list of addresses with pagination."""
    return db.query(models.Address).offset(skip).limit(limit).all()

def create_address(db: Session, address: schemas.AddressCreate):
    """Create a new address record."""
    db_address = models.Address(**address.model_dump())
    db.add(db_address)
    db.commit()
    db.refresh(db_address)
    logger.info(f"Created address ID {db_address.id}: {db_address.name}")
    return db_address

def update_address(db: Session, address_id: int, address_update: schemas.AddressUpdate):
    """Update an existing address."""
    db_address = get_address(db, address_id)
    if db_address:
        update_data = address_update.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_address, key, value)
        db.commit()
        db.refresh(db_address)
        logger.info(f"Updated address ID {address_id}")
    return db_address

def delete_address(db: Session, address_id: int):
    """Delete an address record."""
    db_address = get_address(db, address_id)
    if db_address:
        db.delete(db_address)
        db.commit()
        logger.info(f"Deleted address ID {address_id}")
        return True
    return False

def get_addresses_within_range(db: Session, lat: float, lon: float, radius: float):
    """
    The 'Special Logic': Fetches all addresses and filters those within 
    the given radius using the Haversine formula.
    """
    all_addresses = db.query(models.Address).all()
    nearby_addresses = []
    
    for addr in all_addresses:
        distance = calculate_distance(lat, lon, addr.latitude, addr.longitude)
        if distance <= radius:
            nearby_addresses.append(addr)
            
    logger.info(f"Found {len(nearby_addresses)} addresses within {radius}km of ({lat}, {lon})")
    return nearby_addresses