from llama_index.core import VectorStoreIndex
from llama_index.core import Settings
from llama_index.core import StorageContext, load_index_from_storage
from llama_index.embeddings.gemini import GeminiEmbedding

import sys
from exception import customexception
from logger import logging


def download_gemini_embedding(model, document):
    """
    Downloads and initializes a Gemini Embedding model for vector embeddings.

    Returns:
    - query_engine: An engine to perform similarity queries on the index.
    """
    try:
        logging.info("Initializing Gemini Embedding model...")

        # Use the newer 'text-embedding-004' model
        gemini_embed_model = GeminiEmbedding(model_name="models/text-embedding-004")

        # --- Configure Global Settings (Replaces ServiceContext) ---
        # This sets the configuration for the entire application session
        Settings.llm = model
        Settings.embed_model = gemini_embed_model
        Settings.chunk_size = 800
        Settings.chunk_overlap = 20

        logging.info("Converting documents to vector embeddings (Index)...")
        # Creating the index automatically uses the Settings defined above
        index = VectorStoreIndex.from_documents(document)

        logging.info("Persisting index to storage...")
        # This saves the index to the './storage' folder by default
        index.storage_context.persist()

        logging.info("Creating query engine...")
        query_engine = index.as_query_engine()

        return query_engine

    except Exception as e:
        raise customexception(e, sys)