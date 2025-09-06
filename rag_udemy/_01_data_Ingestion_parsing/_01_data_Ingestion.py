#%%

## Introduction to Data Ingestion
# %%
import os
from typing import List, Dict, Any
from unittest import loader
import pandas as pd
# %%
from langchain_core.documents import Document
from langchain.text_splitter import (
    RecursiveCharacterTextSplitter,
    CharacterTextSplitter,
    TokenTextSplitter,
)
print("Setup Complete")
# %%
## Understanding Document Structure In LangChain
# %%
### create a simple document
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
print(doc)
print(f"{doc.page_content}")
print(f"{doc.metadata}")
print(f"{doc.metadata['source']}")

# why metadata is important?
print("\n Metadata is crucial for:")
print("- Filtering search results")
print("- Tracking document sources")
print("- Providing context in responses")
print("- Debugging and auditing")
print(type(doc))
# %%
### text file (.txt) - the simplest form of text data
os.makedirs('data/text_files', exist_ok=True)

simple_text = {
    "data/text_files/python_intro.txt": """Introduction to Python
Python is a versatile programming language known for its simplicity and readability. It supports multiple programming paradigms, including procedural, object-oriented, and functional programming.

Python is widely used in various fields such as web development, data analysis, artificial intelligence, scientific computing, and more. Its extensive standard library and active community contribute to its popularity.

Key features of Python include:
- Easy to learn and use
- Extensive libraries and frameworks
- Strong community support
- Cross-platform compatibility
- Integration capabilities with other languages and tools

""",
    "data/text_files/machine_learning.txt": """Machine Learning Basics
Machine learning is a subset of artificial intelligence that focuses on building systems that can learn from and make decisions based on data. It involves training algorithms on datasets to identify patterns and make predictions.
There are several types of machine learning, including supervised learning, unsupervised learning, and reinforcement learning. Common algorithms include decision trees, support vector machines, and neural networks.
Applications of machine learning span various domains such as healthcare, finance, marketing, and more. It is used for tasks like image recognition, natural language processing, recommendation systems, and fraud detection.

Key concepts in machine learning include:
- Training and testing datasets
- Model evaluation and validation
- Overfitting and underfitting
- Feature selection and engineering
- Hyperparameter tuning

Types of Machine Learning:
- Supervised Learning: Learning from labeled data
- Unsupervised Learning: Finding patterns in unlabeled data
- Reinforcement Learning: Learning through rewards and penalties

"""}

for file_path, content in simple_text.items():
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Sample text files created.")
# %%
### TextFileLoader - Read Single Text File
from langchain.document_loaders import TextLoader

loader = TextLoader("data/text_files/python_intro.txt", encoding="utf-8")
documents = loader.load()
print(documents)
print(f"Number of documents loaded: {len(documents)}")
print(f"Content of the document:\n{documents[0].page_content}")
print(f"Metadata of the document:\n{documents[0].metadata}")

# %%
### DirectoryLoader - Read Multiple Text Files from a Directory
from langchain_community.document_loaders import DirectoryLoader
from langchain.document_loaders import TextLoader

loader = DirectoryLoader(
    "data/text_files", 
    glob="**/*.txt",
    loader_cls=TextLoader,
    loader_kwargs={"encoding": "utf-8"},
    show_progress=True
)
documents = loader.load()
print(f"Number of documents loaded: {len(documents)}")
for i, doc in enumerate(documents):
    print(f"\nDocument {i+1} Content:\n{doc.page_content[:200]}...")  # Print first 200 characters
    print(f"Metadata: {doc.metadata}")

# %%
### text splitting - splitting large documents into smaller chunks
# Why text splitting is important?
print("\nText splitting is important for:")
print("- Efficient processing and embedding")
print("- Improved search relevance")
print("- Handling model input size limitations")
print("- Better context management")
# %%
from langchain.text_splitter import (
    CharacterTextSplitter,
    RecursiveCharacterTextSplitter,
    TokenTextSplitter,
)

print(documents)
print(documents[0].page_content)
# %%
#### method 1: CharacterTextSplitter
text_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=500,
    chunk_overlap=100,
    length_function=len,
)
texts = text_splitter.split_text(documents[0].page_content)
print(f"Number of chunks created: {len(texts)}")

for i, chunk in enumerate(texts):
    print(f"\nChunk {i+1}:\n{chunk}")
# %%
