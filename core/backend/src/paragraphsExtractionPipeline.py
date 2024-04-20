import json
from cleaner import Cleaner
from paragraphAdapter import paragraphAdapter
from consts import TEST_PDF_LOCATION
from extractor import Extractor
from gptconnector import GPTConnector


class ParagraphsExtractionPipeline:
    @staticmethod
    def run():
        extracted = Extractor.pdf_to_string(TEST_PDF_LOCATION)
        gpt_connector = GPTConnector()
        cleaned_text = Cleaner.clean(extracted)
        #print(cleaned_text)

        # avoiding unexpected behavior by repeating the process
        for _ in range(10):
            try:
                jsonParagraphs = gpt_connector.split_into_paragraphs(cleaned_text).content
                paragraphs_as_list = json.loads(jsonParagraphs)
                pydantic_paragraphs = paragraphAdapter.adapt(paragraphs_as_list)
                print(pydantic_paragraphs)
                break
            except Exception as e:
                continue