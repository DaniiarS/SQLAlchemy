from sqlalchemy import create_engine

SQL_ALCHEMY_URL = "sqlite+pysqlite:///:memory"

# Create Engine: SQLAlchemy's Core
# NOTE: "The Engine, when first returned by create_engine(), has not actually tried to connect to the database yet; 
#        that happens only the first time it is asked to perform a task against the database. 
#        This is a software design pattern known as LAZY INITIALIZATION."
engine = create_engine(url=SQL_ALCHEMY_URL,echo=True)