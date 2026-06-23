import os
import psycopg2

from dotenv import load_dotenv

load_dotenv()

conn = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD")
)

cursor = conn.cursor()

def insert_chunk(
    source,
    chunk_index,
    content,
    embedding,
    commit=True
):
    query = """
        INSERT INTO chunks (source, chunk_index, content, embedding)
        VALUES (%s, %s, %s, %s);
    """

    cursor.execute(
        query,
        (
            source,
            chunk_index,
            content,
            embedding.tolist()
        )
    )

    if commit:
        conn.commit()