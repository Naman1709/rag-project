from app.database import conn, cursor

create_extension_query = "CREATE EXTENSION IF NOT EXISTS vector;"

create_table_query = """
CREATE TABLE IF NOT EXISTS chunks (
    id SERIAL PRIMARY KEY,

    source TEXT NOT NULL,
    chunk_index INTEGER NOT NULL,

    content TEXT NOT NULL,

    embedding VECTOR(384) NOT NULL,

    created_at TIMESTAMP DEFAULT NOW()
);
"""

cursor.execute(create_extension_query)
cursor.execute(create_table_query)

conn.commit()

print("Tables created successfully.")