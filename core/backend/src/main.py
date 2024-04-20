from openai import OpenAI
import fitz
import os  
from consts import RESOURCES_LOCATION

class ChatBot:
    def __init__(self):
        self.client = OpenAI()
        self.engine = "gpt-3.5-turbo"

    # Chat with chatgpt
    def chat(self, question):
        completion = self.client.chat.completions.create(
            model=self.engine,
            messages=[
                {"role": "system", "content": "You are a knowledgeable assistant, ready to answer your questions."},
                {"role": "user", "content": question}
            ]
        )
        return completion.choices[0].message
  
    # Cleans the text
    def clean(self, dirtyText):
        completion = self.client.chat.completions.create(
            model=self.engine,
            messages=[
                {"role": "system", "content": "Your role is to clean the text for me and make it more readable."},
                {"role": "user", "content": dirtyText}
            ]
        )
        return completion.choices[0].message

# Example usage
""" bot = ChatBot()
response = bot.chat("What is the capital of France?")
print(response)
response = bot.clean("C-!iao! C?om...E sZai=?")
print(response) """


class PDFExtractor:
    @staticmethod
    def pdf_to_string(input_pdf_path):
        # Apre il documento PDF
        pdf_doc = fitz.open(input_pdf_path)
        text = ""

        for page in pdf_doc:
            text += page.get_text()

        pdf_doc.close()
        return text

    @staticmethod
    def pdf_to_txt(input_pdf_path, output_txt_path):
        text = PDFExtractor.pdf_to_string(input_pdf_path)
        with open(output_txt_path, "w") as output_txt:
            output_txt.write(text)
            
path = os.path.join(RESOURCES_LOCATION,"WW2.pdf")
extracted = PDFExtractor.pdf_to_string(path)
print(extracted)