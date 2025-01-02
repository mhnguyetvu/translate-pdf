import os
from dotenv import load_dotenv
from pdf_processing.extract_text import extract_text_from_pdf
from pdf_processing.translate_text import translate_text
from pdf_processing.save_translations import save_translated_text
# from utils.file_handler import load_config  # Remove the load_config import


def main():
    # Load environment variables from the .env file
    load_dotenv()

    # Get the OpenAI API key from the environment variable
    openai_api_key = os.getenv("OPENAI_API_KEY")

    if not openai_api_key:
      print("Error: OpenAI API key not found in .env or environment.")
      return
    
    # Use relative paths
    input_pdf = "c:\\Users\\nguyetnvm\\Downloads\\machine_translation_using_NLP.pdf"  # Assuming it's in the same dir or can be accessed
    output_file = "C:\\Users\\nguyetnvm\\Documents\\8. Git-Nguyet\\translate-pdf\\results\\translated_output.txt"  # Save the output in a results folder

    # Create the output directory if it doesn't exist
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    print("Extracting text from PDF...")
    try:
        text = extract_text_from_pdf(input_pdf)
    except Exception as e:
        print(f"Error extracting text: {e}")
        return


    print("Translating text...")
    try:
      translated_text = translate_text(text, openai_api_key, target_language="vi")
    except Exception as e:
      print(f"Error translating text: {e}")
      return

    print("Saving translated text...")
    try:
        save_translated_text(translated_text, output_file)
    except Exception as e:
        print(f"Error saving translated text: {e}")
        return

    print(f"Translation saved to {output_file}.")


if __name__ == "__main__":
    main()