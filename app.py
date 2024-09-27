import streamlit as st
from embedding_model import get_embedding_model
from language_model import query_language_model
from chunking import chunk_text
from utils import convert_pdf_to_text
import os
from language_model import find_closest_chunk
from dotenv import load_dotenv
#from langchain_groq import ChatGroq
from groq import Groq
import logging
os.environ["GROQ_API_KEY"] ="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"
# Configure logging
logging.basicConfig(
    level=logging.DEBUG,  # Change to logging.INFO or logging.ERROR depending on your preference
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(),  # Log to console
        logging.FileHandler("app.log"),  # Log to file (app.log)
    ]
)

logging.info("Logging setup complete.")

# Clear the cache
st.cache_data.clear()

# Title of the app
st.title("PDF ChatBot")

# Step 1: Upload a research paper (PDF)
st.write("Please upload your paper in PDF format.")
uploaded_file = st.file_uploader("Upload a Research Paper (PDF)", type="pdf")

# Debugging: Check if the file is uploaded
st.write("File upload status: ", uploaded_file is not None)

if uploaded_file is not None:
    # Step 2: Convert the uploaded PDF to text
    try:
        text = convert_pdf_to_text(uploaded_file)
        st.write("PDF uploaded and converted to text successfully.")
    except Exception as e:
        st.write(f"Error converting PDF to text: {e}")
    
    # Step 3: Chunk the text for better processing
    max_tokens = st.slider("Select Max Tokens per Chunk", 256, 1024, 512)
    chunks = chunk_text(text, max_tokens=max_tokens)
    st.write(f"Text has been chunked into {len(chunks)} parts.")
    
    # Step 4: Select an embedding model from the dropdown
    embedding_model_name = st.selectbox(
        'Select Embedding Model',
        ['all-MiniLM-L6-v2', 'paraphrase-MiniLM-L12-v2', 'multi-qa-MiniLM-Cos-v1','GritLM/GritLM-7B','nvdia/NV-Embed-v2','BAAI/llm-embedder']
    )
    
    # Load the embedding model
    try:
        model = get_embedding_model(embedding_model_name)
        st.write(f"Embedding model '{embedding_model_name}' loaded successfully.")
    except Exception as e:
        st.write(f"Error loading embedding model: {e}")
    
    # Step 5: Generate embeddings for the chunks
    try:
        embeddings = [model.encode(chunk) for chunk in chunks]
        st.write("Embeddings generated for the research paper.")
    except Exception as e:
        st.write(f"Error generating embeddings: {e}")
    
    # Step 6: Select a language model for querying
    language_model_name = st.selectbox(
        'Select Language Model',
     #  ['flan-t5-xxl', 'gpt-neo-2.7B']
       ['gemma2-9b-it', 'llama-3.1-8b-instant','gemma-7b-it',' mixtral-8x7b-32768',]
    )
    
    # Step 7: User inputs a query
    query = st.text_input("Enter your query:")
    
    if query:
        # Step 8: Process the query with the language model
        try:
            query_embedding=model.encode(query)
            closest_chunk_idx = find_closest_chunk(query_embedding, embeddings)
            print(chunks[closest_chunk_idx],query)

        # Debugging: Log the closest chunk index
            logging.debug(f"Closest chunk index: {closest_chunk_idx}")

        # Generate a response based on the closest chunk
            logging.info("Generating a response using the closest chunk.")
            CONTENT=chunks[closest_chunk_idx]+query
            query_response = query_language_model(CONTENT, language_model_name)
            st.write("Response from language model:")
            st.write(query_response)
        except Exception as e:
            st.write(f"Error querying language model: {e}")
    else:
        st.write("Please upload a PDF file to proceed.")
