# Retrieval-Augmented Generation (RAG)

## What is RAG?

RAG is a technique that combines the power of large language models with external knowledge retrieval. Instead of relying solely on pre-trained knowledge, RAG systems retrieve relevant information from external sources (like databases, documents, or APIs) and use that context to generate more accurate and up-to-date responses.

## How it Works

1. **Query Processing** - User input is processed and converted into searchable format
2. **Retrieval** - Relevant documents/data are retrieved from knowledge base
3. **Augmentation** - Retrieved context is combined with the original query
4. **Generation** - LLM generates response using both query and retrieved context

## Learning Path
1. Learn about vector embeddings and similarity search
2. Explore vector databases (Pinecone, Chroma, FAISS)
3. Practice with RAG frameworks (LangChain, LlamaIndex)
4. Build simple RAG applications
5. Study evaluation metrics for RAG systems

## Common Use Cases
- Question answering systems
- Document chat applications
- Knowledge base assistants
- Customer support bots

## Lessons

### Setup
```
uv init
uv venv
source venv/bin/activate
uv add -r requirements.txt 
pip install ipykernel
```
