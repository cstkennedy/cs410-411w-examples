from __future__ import annotations

from typing import List, Optional

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

"""
class User:
    def __init__(self, nme: str, fullname: str, addresses: list[Address]):
        self.name = nme
        self.fullname = fullname
        self.addresses= addresses
"""

"""
@dataclass
class User:
    name: str = ""
    fullname: str = ""
    addresses: list[Address] = field(default_factory=list)
"""


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "user_account"

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[Name] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )

    addresses: Mapped[list[Address]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )

    def number_of_emails(self) -> int:
        return len(self.addresses)

    def __repr__(self) -> str:
        return " ".join([
            f"User(id={self.id!r},",
            f"name={self.name!r},",
            f"fullname={self.fullname!r},"
            f"addresses={self.addresses!r})"
            ]
        )

    def __str__(self):
        addresses_str = ", ".join(str(addr) for addr in self.addresses)
        return "\n".join(
            (
                f"Full Name: {self.name}",
                f"Emails:    {addresses_str}",
            )
        )

class Name(Base):
    __tablename__ = "name"

    id: Mapped[int] = mapped_column(primary_key=True)
    first: Mapped[str] = mapped_column(String(30))
    last: Mapped[str] = mapped_column(String(30))

    user_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"))
    user: Mapped[User] = relationship(back_populates="name")

    def __str__(self) -> str:
        return f"{self.first} {self.last}"


class Address(Base):
    __tablename__ = "address"

    id: Mapped[int] = mapped_column(primary_key=True)
    email_address: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"))

    user: Mapped["User"] = relationship(back_populates="addresses")

    def split(self) -> list[str]:
        return self.email_address.split("@")

    def __repr__(self) -> str:
        return f"Address(id={self.id!r}, email_address={self.email_address!r})"

    def __str__(self) -> str:
        return self.email_address
