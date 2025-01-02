import openai

def translate_text(text, api_key, target_language="vietnamese"):
    """
    Translates text using OpenAI's API.

    Args:
        text (str): The text to translate.
        api_key (str): Your OpenAI API key.
        target_language (str): The target language for translation (default: English - "en").

    Returns:
        str: The translated text.
    """
    try:
        # Set the OpenAI API key
        openai.api_key = api_key

        # Prepare the translation prompt
        prompt = f"Translate the following text into {target_language}:\n\n{text}"

        # Call the OpenAI API for translation
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": f"You are a helpful assistant that translates text to {target_language}."},
                {"role": "user", "content": text}
            ]
        )
             # Extract and return the translated text
        return response["choices"][0]["message"]["content"].strip()

    except Exception as e:
        print(f"An error occurred during translation: {e}")
        return ""