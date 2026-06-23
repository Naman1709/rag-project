# RAG Information Retrieval System

A Retrieval-Augmented Generation (RAG) pipeline being developed using Python, PostgreSQL (pgvector), FastAPI, and Sentence Transformers.

## Overview

This project focuses on building the retrieval layer of a RAG system. It ingests text documents, splits them into chunks, generates vector embeddings, stores them in PostgreSQL using pgvector, and retrieves relevant context using semantic similarity search.

The current implementation focuses on document ingestion and retrieval. LLM-based answer generation and API endpoints are planned for future development.

---

## Features

### Document Ingestion

* Load text documents from local files
* Process large documents into manageable chunks

### Text Chunking

* Configurable chunk size
* Overlapping chunks to preserve context

### Embedding Generation

* Uses Sentence Transformers
* Generates dense vector representations for semantic search

### Vector Database Storage

* PostgreSQL with pgvector extension
* Stores document chunks and embeddings

### Semantic Retrieval

* Converts user queries into embeddings
* Retrieves the most relevant document chunks using vector similarity(cosine similarity)

---

## Tech Stack

* Python
* PostgreSQL
* pgvector
* Sentence Transformers
* Psycopg2

---

## Current Project Structure

app/
├── api/
│ └── routes.py
├── ingest/
│ ├── loader.py
│ ├── chunker.py
│ ├── embedder.py
│ └── pipeline.py
├── retrieval/
│ └── search.py
├── config.py
├── database.py
└── main.py

---

## Retrieval Workflow

1. Load raw document
2. Split into chunks
3. Generate embeddings
4. Store chunks and vectors in PostgreSQL
5. Convert query into embedding
6. Perform similarity search
7. Return top relevant chunks

---

## Planned Improvements

* FastAPI REST API
* LLM integration
* Context building pipeline
* Chat interface
* Metadata filtering
* Hybrid search
* Evaluation metrics
* Docker deployment

---

## Learning Goals

This project was created to understand the internal components of Retrieval-Augmented Generation systems, including document processing, vector embeddings, semantic search, and knowledge retrieval.

## Status

🚧 Work in Progress

Current stage:

* Document ingestion
* Chunking
* Embedding generation
* Semantic retrieval

Planned:

* API layer
* LLM response generation
* End-to-end chatbot experience
