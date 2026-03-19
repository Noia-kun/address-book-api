from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# SQLite database file path
SQLALCHEMY_DATABASE_URL = "sqlite:///./address_book.db"

# 'check_same_thread' is only needed for SQLite
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency to get the DB session for our routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()