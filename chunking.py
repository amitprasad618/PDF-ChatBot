import re
import logging

def chunk_text(text, max_tokens=512):
    """
    Custom text chunking by splitting the text into chunks of a maximum number of tokens.
    """
    logging.info("Starting text chunking.")
    
    if not text:
        logging.error("Input text is empty.")
        raise ValueError("Input text is empty.")
    
    try:
        sentences = re.split(r'(?<=[.!?])\s+', text)  # Tokenize by sentence
        logging.info(f"Text successfully split into {len(sentences)} sentences.")
        
        chunks = []
        current_chunk = []
        token_count = 0
        
        for i, sentence in enumerate(sentences):
            sentence_tokens = len(sentence.split())
            logging.debug(f"Processing sentence {i+1} with {sentence_tokens} tokens.")
            
            if token_count + sentence_tokens > max_tokens:
                logging.info(f"Chunk reached max token limit. Creating new chunk at sentence {i+1}.")
                chunks.append(" ".join(current_chunk))
                current_chunk = [sentence]
                token_count = sentence_tokens
            else:
                current_chunk.append(sentence)
                token_count += sentence_tokens
        
        # Append the last chunk if any
        if current_chunk:
            chunks.append(" ".join(current_chunk))
            logging.info("Final chunk created.")
        
        logging.info(f"Total chunks created: {len(chunks)}")
        return chunks
    
    except Exception as e:
        logging.error(f"Error during text chunking: {e}", exc_info=True)
        raise ValueError(f"Error during text chunking: {e}")
