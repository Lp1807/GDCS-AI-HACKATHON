from openai import OpenAI

class ChatBot:
    def __init__(self):
        self.client = OpenAI()

    # Chat with chatgpt
    def chat(self, question):
        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a knowledgeable assistant, ready to answer your questions."},
                {"role": "user", "content": question}
            ]
        )
        return completion.choices[0].message
  
    # Cleans the text
    def clean(self, dirtyText):
        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Your role is to clean the text for me and make it more readable."},
                {"role": "user", "content": dirtyText}
            ]
        )
        return completion.choices[0].message

# Example usage
bot = ChatBot()
response = bot.chat("What is the capital of France?")
print(response)
response = bot.clean("C-!iao! C?om...E sZai=?")
print(response)