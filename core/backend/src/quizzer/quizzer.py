import json

from consts import GENERATE_QUESTION_PROMPT, QUIZ_EXAMPLE_LOCATION, GENERATED_QUIZ_LOCATION
from gptconnector import GPTConnector
from quizzer.utils.random_context_creator import RandomContextCreator
from database.vectordb import ChromaDB


class Quizzer:

    def __init__(self, chromadb: ChromaDB, gpt: GPTConnector):
        self.chromadb = chromadb
        self.gpt = gpt
        pass

    def generate_and_save_quiz(self, pdf_name: str) -> dict:
        rcc = RandomContextCreator(chromadb=self.chromadb)

        answers = []
        for i in range(0, 10):
            context, ids = rcc.create_random_context(collection_name=pdf_name)

            print(f"ids: {ids}")

            with open(QUIZ_EXAMPLE_LOCATION, "r") as f:
                example = f.read().replace("\n", "")

            with open(GENERATE_QUESTION_PROMPT, "r") as f:
                prompt = f.read().replace("\n", "")

            print(f"prompt: {prompt}")

            prompt = prompt.format(context=context, example=example, ids=ids)
            print(f"prompt: {prompt}")

            answer = self.gpt.chat(prompt).content

            answers.append(answer)

        answers = "[" + ", ".join(answers) + "]"

        with open(GENERATED_QUIZ_LOCATION, "w") as f:
            f.write(answers)

        print(answers)

        return answers



