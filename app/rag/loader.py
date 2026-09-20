from pathlib import Path
import re
DATA_DIR = Path("data")


def load_documents():
    documents = []

    for file_path in DATA_DIR.glob("*.txt"):
        content = file_path.read_text(encoding="utf-8")
        id = re.search(r"Document ID:\s*([^\n]+)", content)
        title =re.search(r"Title:\s*([^\n]+)", content)
        category =re.search(r"Category:\s*([^\n]+)", content) 

        if title:
            doc_title = title.group(1).strip()
        else:
            doc_title = "N/A"
        
        if category:
            doc_category = category.group(1).strip()
        else:
            doc_category = "N/A"

        if id:
            doc_id = id.group(1).strip()
        else:
            doc_id = file_path.stem
        documents.append({
            "filename": file_path.name,
            "content": content,
            "document_id": doc_id,
            "title": doc_title,
            "category": doc_category
        })

    return documents


if __name__ == "__main__":
    documents = load_documents()

    for document in documents:
        print(document["filename"])
        print(document["content"][:100])
        print("-" * 50)