
# Data Ingestion and Document Processing

## Overview
This module demonstrates the fundamentals of data ingestion and document processing using LangChain, focusing on document structure and metadata management for RAG (Retrieval-Augmented Generation) systems.

## Lesson 01: Document Structure and Metadata

### Objective
Understand the structure of LangChain Document objects and the significance of metadata in RAG systems.

### Dependencies
- `langchain_core.documents` - Core document handling

### Document Structure
The code demonstrates how to create and work with LangChain Document objects:

```python
from langchain_core.documents import Document

# Create a simple document with content and metadata
doc = Document(
    page_content="This is the main content that will be embedded and searched.",
    metadata={
        "source": "example.txt", 
        "page": 1, 
        "author": "azwri",
        "date_created": "2025-09-04",
        "custom_field": "any_value"
    }
)

# Access document properties
print(doc.page_content)  # Main content
print(doc.metadata)      # Metadata dictionary
print(doc.metadata['source'])  # Specific metadata field
```

### Importance of Metadata
Metadata plays a crucial role in RAG systems for:
- **Filtering search results** - Enable targeted retrieval
- **Tracking document sources** - Maintain data lineage
- **Providing context in responses** - Enhance answer quality
- **Debugging and auditing** - Facilitate system maintenance

### Key Features
- Document objects contain both content and metadata
- Metadata can include custom fields for specific use cases
- Proper metadata structure improves retrieval accuracy
- Essential foundation for building effective RAG pipelines

---

## Lesson 02: Text File Creation and Loading

### Objective
Learn how to create sample text files and ingest them using LangChain loaders for RAG pipelines.

### Dependencies
- `os` (standard library)
- `langchain.document_loaders.TextLoader`
- `langchain_community.document_loaders.DirectoryLoader`

### Steps Covered

1. **Create Sample Text Files**
   - Programmatically generate `.txt` files with educational content.

2. **Load a Single Text File**
   - Use `TextLoader` to read and inspect a single file’s content and metadata.

3. **Load Multiple Text Files from a Directory**
   - Use `DirectoryLoader` to batch load all `.txt` files in a folder.

### Code Example

```python
# Create sample text files
os.makedirs('data/text_files', exist_ok=True)
# ...code for writing files...

# Load a single file
from langchain.document_loaders import TextLoader
loader = TextLoader("data/text_files/python_intro.txt", encoding="utf-8")
documents = loader.load()
print(documents[0].page_content)
print(documents[0].metadata)

# Load multiple files
from langchain_community.document_loaders import DirectoryLoader
loader = DirectoryLoader(
    "data/text_files",
    glob="**/*.txt",
    loader_cls=TextLoader,
    loader_kwargs={"encoding": "utf-8"},
    show_progress=True
)
documents = loader.load()
for doc in documents:
    print(doc.page_content[:200])
    print(doc.metadata)
```

### Key Takeaways
- Automate creation of sample data for ingestion.
- Use LangChain loaders to read and process text files.
- Metadata is automatically extracted and attached to each document.
