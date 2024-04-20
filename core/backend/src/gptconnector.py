from openai import OpenAI
from openai.types.chat import ChatCompletionMessage


class GPTConnector:
    def __init__(self):
        self.client = OpenAI()
        self.engine = "gpt-3.5-turbo"

    # Chat with chatgpt
    def chat(self, question: str) -> ChatCompletionMessage:
        completion = self.client.chat.completions.create(
            model=self.engine,
            messages=[
                {"role": "system", "content": "You are a knowledgeable assistant, ready to answer your questions."},
                {"role": "user", "content": question}
            ]
        )
        return completion.choices[0].message

    # Cleans the text
    def clean(self, dirty_text: str) -> ChatCompletionMessage:
        completion = self.client.chat.completions.create(
            model=self.engine,
            messages=[
                {"role": "system", "content": "Your role is to clean the text for me and make it more readable."},
                {"role": "user", "content": dirty_text}
            ]
        )
        return completion.choices[0].message
