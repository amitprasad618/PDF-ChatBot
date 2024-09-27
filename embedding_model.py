import logging
from sentence_transformers import SentenceTransformer
import os
from dotenv import load_dotenv
#from langchain_groq import ChatGroq
#from groq.runtime import GroqModel
#model = GroqModel('gpt-neo-2.7B')


def get_embedding_model(model_name):
    """
    Load and return the embedding model from SentenceTransformers, with logging.
    """
    logging.info(f"Attempting to load embedding model: {model_name}")
    
    try:
        # Load the SentenceTransformer model
        model = SentenceTransformer(f"sentence-transformers/{model_name}")
        #model = GroqModel('{model_name}')

        # Log the successful loading of the model
        logging.info(f"Successfully loaded embedding model: {model_name}")
        return model
    
    except Exception as e:
        # Log any errors encountered during model loading
        logging.error(f"Error loading the embedding model {model_name}: {e}", exc_info=True)
        raise ValueError(f"Error loading the embedding model: {e}")
