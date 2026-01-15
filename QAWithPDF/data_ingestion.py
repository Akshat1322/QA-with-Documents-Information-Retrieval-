from llama_index.core import SimpleDirectoryReader
import sys
from exception import customexception
from logger import logging


def load_data(data):
    """
    Load PDF documents from a specified directory.

    Parameters:
    - data (str): The path to the directory containing PDF files.

    Returns:
    - A list of loaded PDF documents.
    """
    try:
        logging.info("Data loading started...")

        # CORRECTED: Use the variable 'data', not the string "Data"
        loader = SimpleDirectoryReader(data)
        documents = loader.load_data()

        logging.info("Data loading completed...")
        return documents

    except Exception as e:
        logging.info("Exception occurred in loading data...")
        raise customexception(e, sys)