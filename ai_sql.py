import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.utilities import SQLDatabase

load_dotenv()

db = SQLDatabase.from_uri("sqlite:///sample.db")

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0
)

def generate_ai_sql(question):
    schema = db.get_table_info()

    prompt = f"""
You are an expert SQLite SQL generator.

Database Schema:
{schema}

Task:
Convert the user's natural language question into a valid SQLite SQL query.

Rules:
1. Return ONLY the SQL query.
2. Do NOT include explanations.
3. Do NOT use markdown or ```sql.
4. Use ONLY the tables and columns present in the schema.
5. Never invent table names or column names.
6. If aggregation is needed, use SUM(), COUNT(), AVG(), MAX(), or MIN() as appropriate.
7. If the question asks for the "top" or "highest", use ORDER BY ... DESC LIMIT 1.
8. If the question asks for monthly data, use the month column exactly as it appears in the schema.
9. Generate SQL compatible with SQLite.
10. If the question cannot be answered using the given schema, return exactly:
INVALID QUERY

User Question:
{question}
"""

    response = llm.invoke(prompt)
    return response.content.strip()