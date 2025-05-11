import engine
from sqlalchemy import text

# Sending Prameters
# "Executemany" style - INSERT command is executed for every dictionary in the list passed as parameters
with engine.engine.connect() as conn:
    conn.execute(text("INSERT INTO some_table (x, y) VALUES (:x, :y)"), [{"x": 10, "y": 20},{"x": 30, "y": 40}])
    conn.commit()