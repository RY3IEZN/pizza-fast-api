# manually update the db without using alembic

from db_setup import engine, Base
from models.user import User, Order

Base.metadata.create_all(bind=engine)
