from app.rag.chunker import chunk_text


def test_chunk_creation():
    document = {
        "content": "A" * 1000,
        "filename": "test.txt",
        "document_id": "DOC-001",
        "title": "Test Document",
        "category": "Testing"
    }

    chunks = chunk_text(document, chunk_size=500, overlap=50)

    assert len(chunks) == 3

def test_chunk_content():
    document = {
        "content": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "filename": "test.txt",
        "document_id": "DOC-001",
        "title": "Test Document",
        "category": "Testing"
    }

    chunks = chunk_text(document, chunk_size=10, overlap=2)

    assert chunks[0]["content"] == "ABCDEFGHIJ"
    assert len(chunks[0]["content"]) == 10

def test_chunk_metadata():
    document = {
        "content": "This is a test document.",
        "filename": "password_reset.txt",
        "document_id": "DOC-001",
        "title": "Password Reset Procedure",
        "category": "IT Support"
    }

    chunks = chunk_text(document, chunk_size=10, overlap=2)

    metadata = chunks[0]["metadata"]

    assert metadata["source"] == "password_reset.txt"
    assert metadata["Document ID"] == "DOC-001"
    assert metadata["Title"] == "Password Reset Procedure"
    assert metadata["Category"] == "IT Support"

def test_chunk_overlap():
    document = {
        "content": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "filename": "test.txt",
        "document_id": "DOC-001",
        "title": "Test Document",
        "category": "Testing"
    }

    chunks = chunk_text(document, chunk_size=10, overlap=2)

    assert chunks[0]["content"] == "ABCDEFGHIJ"
    assert chunks[1]["content"] == "IJKLMNOPQR"