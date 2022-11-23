from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLITE_DATABASE_URL = "sqlite:///./sqlite_test.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

class Database:
    def __new__(cls):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        cls = type(self)

        if not hasattr(cls, "_init"):
            self._engine = create_engine(
                SQLITE_DATABASE_URL,
                echo=True,
                connect_args={"check_same_thread": False},
            )
            self._session = sessionmaker(
                autocommit=False,
                autoflush=False,
                bind=self._engine)
            cls._init = True

    def get_session(self):
        db_session = self._session()
        try:
            yield db_session
        finally:
            db_session.close()

    @property
    def engine(self):
        return self._engine

    @property
    def session(self):
        return self.get_session


db = Database()