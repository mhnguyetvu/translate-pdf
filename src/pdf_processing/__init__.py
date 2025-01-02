from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_path):
    """
    Extracts text from a PDF file.

    Args:
        pdf_path (str): Path to the PDF file.

    Returns:
        str: Extracted text from the PDF.
    """
    try:
        # Open the PDF file
        reader = PdfReader(pdf_path)
        text = ""

        # Loop through each page and extract text
        for page in reader.pages:
            if page.extract_text():
                text += page.extract_text() + "\n"

        return text.strip()

    except FileNotFoundError:
        print(f"Error: File '{pdf_path}' not found.")
        return ""

    except Exception as e:
        print(f"An error occurred: {e}")
        return ""
