from nicegui import ui

from consts import TEST_PDF_LOCATION
from core.backend.src.extractor import Extractor
from core.backend.src.gptconnector import GPTConnector

# Example usage
""" bot = ChatBot()
response = bot.chat("What is the capital of France?")
print(response)
response = bot.clean("C-!iao! C?om...E sZai=?")
print(response) """

if __name__ == "__main__":
    extracted = Extractor.pdf_to_string(TEST_PDF_LOCATION)
    gpt_connector = GPTConnector()
    cleaned_text = gpt_connector.clean(extracted).content
    print(cleaned_text)



