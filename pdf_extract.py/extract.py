import os
from langchain_community.document_loaders import PyPDFLoader
from typing import Optional

def extract_resume_text(file_path: str) -> Optional[str]:
    """
    Extracts text from a given file path.
    Routes to PDF loader or plain text reader based on the file extension.
    """
    # Extract the file extension to route the logic
    _, file_extension = os.path.splitext(file_path)
    file_extension = file_extension.lower()

    if file_extension == '.pdf':
        try:
            # Initialize LangChain's PDF loader
            loader = PyPDFLoader(file_path)
            docs = loader.load()
            
            # Combine all pages into a single string
            resume_text = "\n".join([doc.page_content for doc in docs])
            return resume_text
        
        except Exception as e:
            print(f"Error processing PDF: {e}")
            return None

    elif file_extension == '.txt':
        try:
            # Read plain text files directly
            with open(file_path, 'r', encoding='utf-8') as file:
                resume_text = file.read()
            return resume_text
            
        except Exception as e:
            print(f"Error processing text file: {e}")
            return None

    else:
        # Handle unexpected file types gracefully
        print(f"Unsupported file format: {file_extension}. Please use .pdf or .txt.")
        return None

# --- Testing the script ---
if __name__ == "__main__":
    # You can test this file directly by running `python extract.py`
    # Replace 'sample_resume.pdf' with a real file path in your directory
    test_file = "sample_resume.pdf" 
    
    if os.path.exists(test_file):
        extracted_content = extract_resume_text(test_file)
        print("Extraction Successful! Here is a preview:")
        print(extracted_content[:200]) # Print first 200 characters
    else:
        print(f"To test, place a file named '{test_file}' in this directory.")