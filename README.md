PDF-chatbot    1. pip install streamlit
2. pip install sentence-transformers
3. pip install groq
4. pip install pdfplumber
5. streamlit run app.py 


PDF Chatbot for Research Papers

Developed an interactive PDF chatbot using Streamlit, enabling users to upload research papers and retrieve relevant information through natural language queries.
Implemented text extraction and chunking techniques, optimizing the processing of PDF documents and facilitating efficient querying with advanced embedding models.
Integrated multiple language models for enhanced response generation, improving user engagement and information accessibility in academic research.



Tech Stack Used
Frontend Framework: Streamlit (for building the interactive web application)
PDF Processing: Custom utility for converting PDF files to text
Natural Language Processing:
Embedding Models: Various models (e.g., MiniLM, GritLM) for generating text embeddings
Language Models: Models like Gemma and LLaMA for query processing and response generation
Chunking: Custom chunking logic for managing text segments
Environment Management: dotenv for managing environment variables (e.g., API keys)
Logging: Python's logging module for monitoring application behavior
Deployment: Streamlit Sharing or similar platform for hosting the application
This stack combines modern NLP techniques with a user-friendly interface, making it suitable for academic and research applications.
