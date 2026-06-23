from app.database import conn
from app.ingest.embedder import embed_text

def retrieve(query, top_k = 5):
    """
    Retrieve relevant documents based on the query.

    Args:
        query (str): The search query.
        top_k (int): The number of top results to return.

    Returns:
        list: A list of relevant documents.
    """

    # SQL query to retrieve the top_k most similar documents based on cosine similarity
    sql_query = """
        SELECT content, source, chunk_index, 1 - (embedding <=> %s::vector) AS similarity
        FROM chunks
        ORDER BY embedding <=> %s::vector
        LIMIT %s;
    """

    query_embedding = embed_text([query])[0]  # Get the embedding for the query
    
    with conn.cursor() as cursor:
        cursor.execute(sql_query, (query_embedding.tolist(), query_embedding.tolist(), top_k))
        results = cursor.fetchall()

        results_objects = [
            {
                "content": row[0],
                "source": row[1],
                "chunk_index": row[2],
                "similarity": row[3]
            }
            for row in results
        ]

    return results_objects


# test the retrieve function
while True:
    query = input("Enter your query (or type 'exit' to quit): ")
    if query.lower() == 'exit':
        break
    results = retrieve(query)
    print(f"Top {len(results)} results:")
    for i, result in enumerate(results):
        print(f"{i + 1}. Source: {result['source']}, Chunk Index: {result['chunk_index']}, Similarity: {result['similarity']:.4f}")
        print(f"   Content: {result['content']}")