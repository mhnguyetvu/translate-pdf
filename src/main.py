from pdf_processing.extract_text import extract_text_from_pdf
from pdf_processing.translate_text import translate_text
from pdf_processing.save_translations import save_translated_text
from utils.file_handler import load_config

def main():
    config = load_config("C:\\Users\\nguyetnvm\\Documents\\8. Git-Nguyet\\translate-pdf\\src\\config\\config.yaml")
    input_pdf = "C:\\Users\\nguyetnvm\\Downloads\\machine_translation_using_NLP.pdf"
    output_file = "C:\\Users\\nguyetnvm\\Documents\\8. Git-Nguyet\\translate-pdf\\results\\translated_output.txt"

    print("Extracting text from PDF...")
    text = extract_text_from_pdf(input_pdf)

    print("Translating text...")
    translated_text = translate_text(text, config["openai"]["api_key"], target_language="vi")

    print("Saving translated text...")
    save_translated_text(translated_text, output_file)

    print(f"Translation saved to {output_file}.")

if __name__ == "__main__":
    main()
