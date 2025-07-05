import os
import openai
import sqlite3
import pandas as pd
from dotenv import load_dotenv

# Load the API key
load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Connect to SQLite
conn = sqlite3.connect("company.db")

# User question
user_question = input("Ask your question: ")

# Prompt for GPT
prompt = f"""
Convert this natural language question to SQL:
"{user_question}"
Only return the SQL query, nothing else.
The table is named 'employees' and has columns: id, name, department, salary.
"""

# Call the model using new v1 interface
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": prompt}
    ]
)

# Extract generated SQL
sql_query = response.choices[0].message.content.strip()

print(f"\nGenerated SQL:\n{sql_query}")

# Execute SQL
try:
    df = pd.read_sql_query(sql_query, conn)
    print("\nQuery Result:\n", df)
except Exception as e:
    print("⚠️ Error executing query:", e)

conn.close()
