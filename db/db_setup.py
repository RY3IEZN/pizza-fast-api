from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


SQLALCHEMY_DATABASE_URL = "postgresql://uneku:pgadmin@18.171.190.230:5432/pizzadb"

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True, connect_args={}, future=True)


Base = declarative_base()

SessionLocal = sessionmaker(future=True, autocommit=False, autoflush=False, bind=engine)


# get the db
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
