from unittest import TestCase
from quizzer.quizzer import Quizzer
from gptconnector import GPTConnector
from database.vectordb import ChromaDB
from consts import TEST_PDF_SHORT_LOCATION


class TestQuizzer(TestCase):
    
    def test(self):
        chromaDB = ChromaDB()
        gpt = GPTConnector()
        
        quizzer = Quizzer(chromaDB, gpt)
        pdf_name = TEST_PDF_SHORT_LOCATION.split("/")[-1]
        quizzer.generate_questions(pdf_name)

