from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker

engine = create_engine('sqlite:///database.db', echo=True)
base = declarative_base()

class User(base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)

base.metadata.create_all(engine)

session = sessionmaker(bind=engine)()

user1 = User(name="Иван", fullname="Иванов")
session.add(user1)
session.commit()

q = session.query(User).filter_by(name="Иван")
other_user = q.first()

other_user = User(name="Иван", fullname="Иванов")
session.add(other_user)
session.commit()

other_user = User(name="Сергей", fullname="Светлый")
session.add(other_user)
session.commit()

other_user.fullname = "Петр"
session.commit()
