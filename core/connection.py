import engine
from sqlalchemy import text


# NOTE: The purpose of the Engine is to connect to the database by providing a Connection object. 
#       When working with the Core directly, the Connection object is how all interaction with the database is done. 
#       Because the Connection creates an open resource against the database, we want to limit our use of this object 
#       to a specific context.
#       With Connection the transaction is NOT COMMITTED automatically
with engine.engine.connect() as conn:
    result = conn.execute(text("select 'hello world'"))
    print(result.all())


# "Commit As You Go" style
with engine.engine.connect() as conn:
    conn.execute(text("CREATE TABLE some_table (x int, y int)"))
    conn.execute(text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),[{"x": 1, "y": 2}, {"x": 3, "y": 4}])

    conn.commit()


# "Begin Once" style
with engine.engine.begin() as conn:
    conn.execute(text("INSERT INTO some_table (x, y) VALUES (:x, :y)"), [{"x": 5, "y": 6}])