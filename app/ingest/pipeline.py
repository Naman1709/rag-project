from app.ingest.loader import load_text_from_file
from app.ingest.chunker import chunk_text
from app.ingest.embedder import embed_text
from app.database import insert_chunk, conn
import os
from dotenv import load_dotenv

load_dotenv()
file_paths = os.getenv("FILE_PATHS").split(",")  # Assuming FILE_PATHS is a comma-separated list of file paths

if __name__ == "__main__":
    # Load text from file
    print(f"Loading text from {file_paths[0]}...")
    text = load_text_from_file(file_paths[0])  # Load the first file for testing
    print("Text loaded successfully.")

    # Chunk the text
    print("Chunking text...")
    chunks = chunk_text(text)
    print(f"Text chunked into {len(chunks)} chunks.")

    # Embed each chunk
    print("Generating embeddings for each chunk...")
    embeddings = embed_text(chunks)
    print(f"Generated embeddings for {len(embeddings)} chunks.")

    # Insert chunks and embeddings into the database
    print("Inserting chunks and embeddings into the database...")
    for i, (chunk, embedding) in enumerate(zip(chunks, embeddings)):
        insert_chunk(
            source=file_paths[0].split("/")[-1],  # Use the file name as the source
            chunk_index=i,
            content=chunk,
            embedding=embedding,
            commit=False  # Defer commit until all inserts are done
        )
        
    conn.commit()  # Commit all inserts at once
    print("Chunks and embeddings inserted successfully.")