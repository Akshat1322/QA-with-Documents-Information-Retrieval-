import os
from dotenv import load_dotenv
import sys

from llama_index.llms.gemini import Gemini
from exception import customexception
from logger import logging

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")


def load_model():
    """
    Loads a Gemini model for natural language processing.

    Returns:
    - Gemini: An instance of the Gemini class initialized with the 'gemini-1.5-flash' model.
    """
    try:
        logging.info("Initializing Gemini Model (gemini-1.5-flash)...")

        if not GOOGLE_API_KEY:
            raise ValueError("GOOGLE_API_KEY not found in environment variables.")

        # 'model' is the correct parameter name (not 'models')
        # Using gemini-1.5-flash for better speed/cost balance in RAG
        model = Gemini(
            model="models/gemini-3-flash-preview",
            api_key=GOOGLE_API_KEY
        )
        return model

    except Exception as e:
        raise customexception(e, sys)