from sql_adapter import SQLAdapter


db = SQLAdapter(
    db_type="sqlserver",
    host="localhost",
    port=1433,
    db_name="master",
    username="",  # Not needed
    password=""   # Not needed
)

rows=db.read("Select * from dbo.product")
for row in rows:
    print(row)