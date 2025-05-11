import engine
from sqlalchemy import text

with engine.engine.begin() as conn:
    result = conn.execute(text("SELECT x, y FROM some_table"))
    for line in result:
        print(f"({line.x},{line.y})")

# Example: execute() with parameters, accpets list of dictionaries, returns iterbale object(named tuples)
with engine.engine.begin() as conn:
    result = conn.execute(text("SELECT x, y FROM some_table WHERE y > :y"), [{"y":2}])
    for line in result:
        print(line)