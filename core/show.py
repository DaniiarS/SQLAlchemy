import engine
from sqlalchemy import text

# Display all the rows in the table
with engine.engine.begin() as conn:
    result = conn.execute(text("SELECT * FROM some_table"))
    for line in result:
        print(line)
