import requests
from sqlalchemy import create_engine,text,MetaData
from config import DATA_BASE_URL,GROQ_API_KEY
import os
from langchain_groq import ChatGroq

def get_db_schema(engine):
    meta = MetaData()
    meta.reflect(bind=engine)
    schema = ""
    for table in meta.tables.values():
        schema += f"\nTable: {table.name}\nColumns: {', '.join([col.name + ' (' + str(col.type) + ')' for col in table.columns])}\n"
    return schema.strip()


def call_groq_api(prompt):
    llm = ChatGroq(
        groq_api_key=GROQ_API_KEY,
        model_name="Llama3-8b-8192",
        temperature=1,
        top_p=0.9
    )
    response = llm.invoke(prompt)
    return response.content.strip()
    

def execute_sql(engine, query):
    with engine.connect() as conn:
        result = conn.execute(text(query))
        return result.fetchall(), result.keys()   