from openai import OpenAI

class ChatBot:
  def __init__(self):
    self.client = OpenAI()

  def chat(self, question):
    completion = self.client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "system", "content": "You are a knowledgeable assistant, ready to answer your questions."},
        {"role": "user", "content": question}
      ]
    )
    return completion.choices[0].message

# Example usage
bot = ChatBot()
response = bot.chat("What is the capital of France?")
print(response)