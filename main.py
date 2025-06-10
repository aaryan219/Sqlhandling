from sql_adapter import SQLAdapter


db = SQLAdapter(
    db_type="sqlserver",
    host="localhost",
    port=1433,
    db_name="chinook",
    username="",  # Not needed
    password=""   # Not needed
)

rows=db.read("Select * from dbo.Artist")
for row in rows:
    print(row)
# rows=db.stream_read("Select * from dbo.Artist")
# for row in rows:
#     print(row)

# db.insert(
#     table="Artist",
#     columns=["ArtistId", "Name"],
#     values=[277, "Alexnader the Great"]
# )
# columns = ["ArtistId", "Name"]
# values_list = [
#     [278, "Aryan the Brave"],   # New entry (should insert)
#     [279, "Data Bard"],         # New entry (should insert)
#     [280, "Aryan the Great"],   # Existing ArtistId (should update)
# ]


# db.bulk_upsert(
#     table="Artist",
#     columns=columns,
#     values_list=values_list,
#     key_columns=["ArtistId"]
# )
