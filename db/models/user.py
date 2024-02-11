from db_setup import Base
from sqlalchemy import Column, Integer, ForeignKey, Boolean, Text, String
from sqlalchemy_utils.types import ChoiceType
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "pizzauser"

    id = Column(Integer, primary_key=True)
    username = Column(String(25), unique=True)
    email = Column(String(80), unique=True)
    password = Column(Text, nullable=True)
    is_staff = Column(Boolean, default=False)
    is_active = Column(Boolean, default=False)

    orders = relationship("Order", back_populates="pizzauser")

    def __repr__(self):
        return f"<user {self.username}"


class Order(Base):
    ORDER_STATUS = (
        ("PENDING", "pending"),
        ("DELIVERED", "delivered"),
        ("IN-TRANSIT", "in-transit"),
    )

    PIZZA_SIZES = (
        ("SMALL", "small"),
        ("MEDIUM", "medium"),
        ("LARGE", "large"),
        ("EXTRA-LARGE", "extra-large"),
    )

    __tablename__ = "orders"
    id = Column(Integer, primary_key=True)
    quantity = Column(Integer, nullable=False)
    order_status = Column(ChoiceType(choices=ORDER_STATUS), default="PENDING")
    pizza_size = Column(ChoiceType(choices=PIZZA_SIZES), default="SMALL")
    user_id = Column(Integer, ForeignKey("pizzauser.id"))
    pizzauser = relationship("pizzauser", back_populates="orders")

    def __repr__(self):
        return f"<Order {self.id}"
