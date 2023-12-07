import os
from dotenv import load_dotenv
from transformers import pipeline
from flask import Flask

load_dotenv()

# Initialize Flask app (if required for your application)
app = Flask(__name__)


def test_html_files(directory="templates/"):
    """Checks if HTML files exist in the specified directory"""
    html_files = [f for f in os.listdir(directory) if f.endswith(".html")]

    for html_file in html_files:
        file_path = os.path.join(directory, html_file)
        assert os.path.exists(file_path) and os.path.isfile(file_path)


def test_huggingface_api():
    """Checks Hugging Face API with a prompt"""
    # Initialize the text generation pipeline
    text_generator = pipeline("text-generation", model="gpt2")

    test_prompt = "The answer to the universe is?"
    response = text_generator(test_prompt, max_length=50, num_return_sequences=1)
    assert response[0]["generated_text"] is not None


# Run the tests when this file is executed directly
if __name__ == "__main__":
    test_html_files()
    test_huggingface_api()
