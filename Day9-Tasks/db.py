from sqlalchemy import create_engine
from model import base
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager


class Database:

    __engine = create_engine('postgres+psycopg2://postgres:vamsi@localhost:5432/hospital')

    Session = sessionmaker(bind=__engine)

    @staticmethod
    def create_database():
        base.metadata.create_all(Database.__engine)

    @contextmanager
    def session_scope():
        session = Database.Session()
        try:
            yield session
            session.commit()
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()


