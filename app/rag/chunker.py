from loader import load_documents
def chunk_text(document, chunk_size=500, overlap=50):
    chunks = []
    text = document["content"]
    start = 0

    while start < len(text):
        end = start + chunk_size

        chunk = {"content": text[start:end],
                 "metadata": {"source": document["filename"],
                              "Document ID": document["document_id"],
                              "Title": document["title"],
                              "Category": document["category"]}}
        chunks.append(chunk)

        start = end - overlap

    return chunks

documents = load_documents()

for document in documents:
    chunks = chunk_text(document)
    print(document["filename"])
    print("Number of chunks:", len(chunks))
    print(chunks[0])