#  db_create.py

from project import db

db.create_all()

db.session.commit()