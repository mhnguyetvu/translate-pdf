def save_translated_text(translated_text, output_path):
    """
    Saves the translated text to a file.

    Args:
        translated_text (str): The text to save.
        output_path (str): Path to the output file.

    Returns:
        None
    """
    try:
        # Open the file in write mode and save the text
        with open(output_path, "w", encoding="utf-8") as file:
            file.write(translated_text)
        print(f"Translated text successfully saved to {output_path}.")
    except Exception as e:
        print(f"An error occurred while saving the file: {e}")
