import numpy as np
from transformers import pipeline
from language_model import query_language_model  # Adjust this import to match where your function is located

def test_query_model():
    test_query = "What are the main findings of the research?"
    test_embeddings = [np.random.rand(768) for _ in range(5)]  # Dummy embeddings
    
    try:
        # Test with gpt-3.5-turbo
      #  result = query_language_model(test_query, test_embeddings, "gpt-3.5-turbo")
       # print("Result with gpt-3.5-turbo:")
       # print(result)
        
        # You can also test with other models if needed
         result = query_language_model(test_query, test_embeddings, "flan-t5-xxl")
         print("Result with flan-t5-xxl:")
         print(result)
        
        # result = query_language_model(test_query, test_embeddings, "gpt-neo-2.7B")
        # print("Result with gpt-neo-2.7B:")
        # print(result)
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_query_model()
