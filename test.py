from langchain_community.utilities import SQLDatabase

db = SQLDatabase.from_uri("sqlite:///sample.db")

print("Connected successfully")
print("Tables:", db.get_usable_table_names())