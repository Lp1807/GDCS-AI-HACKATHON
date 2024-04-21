from consts import GENERATE_QUESTION_PROMPT
from gptconnector import GPTConnector
from quizzer.utils.random_context_creator import RandomContextCreator
from database.vectordb import ChromaDB


class Quizzer:

    def __init__(self, chromadb: ChromaDB, gpt: GPTConnector):
        self.chromadb = chromadb
        self.gpt = gpt
        pass

    def generate_questions(self, pdf_name: str):
        rcc = RandomContextCreator(chromadb=self.chromadb)
        context, ids = rcc.create_random_context(collection_name=pdf_name)

        with open(GENERATE_QUESTION_PROMPT, "r") as f:
            prompt = f.read().replace("\n", "")
        prompt = prompt.format(context=context)
        answer = self.gpt.chat(prompt).content

        print(answer)



