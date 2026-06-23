def chunk_text(text, chunk_size=200, overlap=30):
    words = text.split()
    chunks = []
    start = 0
    n = len(words)

    while start < n:
        end = min(start + chunk_size, n)
        chunk = " ".join(words[start:end])
        chunks.append(chunk)
        start += chunk_size - overlap   # slide window

    return chunks