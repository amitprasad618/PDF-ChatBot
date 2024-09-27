import logging
import numpy as np
from transformers import pipeline
from groq import Groq
'''
# Configure logging
logging.basicConfig(
    level=logging.DEBUG,  # Adjust as needed (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(),  # Log to console
        logging.FileHandler("app.log"),  # Log to file (app.log)
    ]
)
'''
def find_closest_chunk(query_embedding, embeddings):
    """
    Find the closest chunk to the query based on cosine similarity.
    """
    logging.info("Finding closest chunk to the query.")
    try:
        # Log details of the embeddings
     #   logging.debug(f"Query embedding shape: {query_embedding.shape}")
      #  logging.debug(f"Embeddings shape: {embeddings.shape}")
        
        # Calculate cosine similarity
        similarities = np.dot(embeddings, query_embedding) / (
            np.linalg.norm(embeddings, axis=1) * np.linalg.norm(query_embedding)
        )
        closest_idx = np.argmax(similarities)
        
        # Log the index of the closest chunk
        logging.info(f"Closest chunk index: {closest_idx}")
        return closest_idx
    except Exception as e:
        logging.error(f"Error finding closest chunk: {e}", exc_info=True)
        raise ValueError(f"Error finding closest chunk: {e}")

# Log the start of the function
logging.info("Starting the query_language_model function")

def query_language_model(CONTENT, language_model_name):
    """
    Process the query using the selected language model and return the response.
    """
    logging.info(f"Starting query with language model: {language_model_name}")
    try:
        # Load the query language model
        logging.info("Loading language model.")
       #if language_model_name == "flan-t5-xxl":
        #    generator = pipeline('text-generation', model="google/flan-t5-xxl")
    #     if language_model_name == "distil-whisper-large-v3-en":
    #         generator = pipeline('text-generation', model="distil-whisper-large-v3-en")
    #   #  elif language_model_name == "gpt-neo-1.3B":
    #   #     generator = pipeline('text-generation', model="EleutherAI/gpt-neo-2.7B")
    #     elif language_model_name=="llama-3.1-8b-instant":
         #    generator = pipeline('text-generation', model="llama-3.1-8b-instant")
    #     else:
    #         logging.error("Unknown language model specified.")
    #         raise ValueError("Unknown language model")
        client = Groq(
            api_key="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",
                        )

        # Debugging: Log the query and embeddings count
        # logging.debug(f"Query: {query}")
        # logging.debug(f"Number of chunks in embeddings: {len(embeddings)}")

        # # Find the closest chunk
        # logging.info("Encoding the query and finding the closest chunk.")

        ## to get embeddings
        # get_embedding_model(model_name)
        # query_embedding = np.array(generator.tokenizer.encode(query, return_tensors="pt")).numpy()
        # closest_chunk_idx = find_closest_chunk(query, embeddings)

        # Debugging: Log the closest chunk index
        # logging.debug(f"Closest chunk index: {closest_chunk_idx}")

        # Generate a response based on the closest chunk
        logging.info("Generating a response using the closest chunk.")

        chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": CONTENT,
            }
        ],
        model=language_model_name,
        )
        print(chat_completion.choices[0].message.content)
        
        logging.info("Response generated successfully.")
        return chat_completion.choices[0].message.content
    except Exception as e:
        logging.error(f"Error generating response from language model: {e}", exc_info=True)
        raise ValueError(f"Error generating response from language model: {e}")
