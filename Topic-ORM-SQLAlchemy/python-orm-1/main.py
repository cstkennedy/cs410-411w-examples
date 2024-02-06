import logging

from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from models import *


def main():
    engine = create_engine("sqlite+pysqlite:///:memory:", echo=False)
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        users = [
            User(
                name="spongebob",
                fullname="Spongebob Squarepants",
                addresses=[
                    Address(email_address="spongebob@sqlalchemy.org"),
                    Address(email_address="spongebob@crustycrab.com"),
                ],
            ),
            User(
                name="sandy",
                fullname="Sandy Cheeks",
                addresses=[
                    Address(email_address="sandy@sqlalchemy.org"),
                    Address(email_address="sandy@squirrelpower.org"),
                ],
            ),
            User(
                name="squidward",
                fullname="Squidward Tentacles",
                addresses=[
                    Address(email_address="squirdward@sqlalchemy.org"),
                ]
            ),
            User(
                name="patrick",
                fullname="Patrick Star",
                addresses=[Address(email_address="wumbo@wumboing.com")],
            ),
        ]

        session.add_all(users)

        session.commit()

    with Session(engine) as session:
        stmt = (
            select(User)
            .where(User.name.in_(["spongebob", "patrick", "squidward"]))
            .order_by(User.fullname)
        )

        print()
        print("*" * 80)
        for user in session.scalars(stmt):
            #  print(user)
            #  print()
            #  print(repr(user))
            #  print()
            #  print(user.number_of_emails())

            print(f"{user.fullname} has email addresses for the following domains...")
            domains = (email.split()[-1] for email in user.addresses)
            for domain in domains:
                print(f"  - {domain}")


        print("*" * 80)
        print()


if __name__ == "__main__":
    main()
