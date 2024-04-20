from core.backend.src.gptconnector import GPTConnector
from core.backend.src.quizzer.utils.random_context_creator import RandomContextCreator
from core.backend.src.vectordb import ChromaDB


class Quizzer:

    def __init__(self, chromadb: ChromaDB, gpt: GPTConnector):
        self.chromadb = chromadb
        self.gpt = gpt
        pass

    def generate_questions(self, pdf_name: str):
        rcc = RandomContextCreator(chromadb=self.chromadb)
        context = rcc.create_random_context(collection_name=pdf_name)
        prompt = context + "something else"



