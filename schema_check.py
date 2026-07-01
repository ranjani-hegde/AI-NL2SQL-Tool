from langchain_community.utilities import SQLDatabase

db = SQLDatabase.from_uri("sqlite:///sample.db")

print(db.get_table_info())