import pdfplumber
import logging

def convert_pdf_to_text(uploaded_file):
    """
    Convert a PDF file into a text string using pdfplumber.
    """
    logging.info(f"Starting PDF extraction for file: {uploaded_file}")
    
    try:
        text = ""
        with pdfplumber.open(uploaded_file) as pdf:
            logging.info(f"Opened PDF file successfully. Number of pages: {len(pdf.pages)}")
            
            for page_num, page in enumerate(pdf.pages):
                logging.debug(f"Extracting text from page {page_num + 1}")
                page_text = page.extract_text()
                
                if page_text:
                    text += page_text
                else:
                    logging.warning(f"No text found on page {page_num + 1}")
        
        if not text:
            logging.error("No text found in the entire PDF.")
            raise ValueError("No text found in the PDF.")
        
        logging.info("PDF extraction completed successfully.")
        return text
    
    except Exception as e:
        logging.error(f"Error processing PDF: {e}", exc_info=True)
        raise ValueError(f"Error processing PDF: {e}")
