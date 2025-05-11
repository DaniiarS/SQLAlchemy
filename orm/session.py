from sqlalchemy.orm import Session
from sqlalchemy import text
from core.engine import engine

# NOTE: The fundamental transactional / database interactive object when using the ORM is called the Session. 
#       In modern SQLAlchemy, this object is used in a manner very similar to that of the Connection, and in fact 
#       as the Session is used, it refers to a Connection internally which it uses to emit SQL.
statement = text("SELECT x, y FROM some_table WHERE y > :y ORDER BY x, y")
with Session(engine) as session:
    result = session.execute(statement,[{"y": 6}])
    for line in result:
        print(line)

upd_statement = text("UPDATE some_table SET y=:y WHERE x=:x")
with Session(engine) as session:
    session.execute(upd_statement, [{"x": 10, "y": 100}, {"x": 30, "y": 300}])
    session.commit()


# NOTE: The Session doesn’t actually hold onto the Connection object after it ends the transaction. 
#       It gets a new Connection from the Engine the next time it needs to execute SQL against the database.
select_statement = text("SELECT x, y FROM some_table")
with Session(engine) as session:
    result = session.execute(select_statement)
    for line in result:
        print(line)