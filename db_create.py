#  db_create.py

from datetime import date

from project import db
from project.models import Task, User

db.create_all()

db.session.add(
    User("admin", "ad@min.com", "admin", "admin")
)
db.session.add(
    Task("Finish this tutorial", date(2015, 3, 13), 10, date(2015, 2, 13), 1, 1)
)
db.session.add(
    Task("Finish real python", date(2015, 3, 13), 10, date(2015,2, 13), 1, 1)
)

db.session.commit()