from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

from app.infrastructure.config import app_config

Base = declarative_base()

# pool_pre_ping=True as argument if needed
engine = create_engine(app_config.SQL_URI)
Session = scoped_session(sessionmaker(bind=engine,
                                      autocommit=False,
                                      autoflush=True))

# from .log import Log
from .fundamental_entry import FundamentalEntry

Base.metadata.create_all(engine)
