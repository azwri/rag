#%%

## Introduction to Data Ingestion
# %%
import os
from typing import List, Dict, Any
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
# create a simple document
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
# %%
