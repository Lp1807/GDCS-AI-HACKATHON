import json
import os

from connectors import gpt_connector, chromadb
from consts import RESOURCES_LOCATION
from paragraphs_ingester.utils.cleaner import Cleaner
from paragraphs_ingester.utils.paragraphs_adapter import ParagraphsAdapter
from paragraphs_ingester.utils.pdf2text import PDF2Text


class ParagraphsIngester:
    @staticmethod
    def run(pdf_path: str):
        """ Populate Vector Database with paragraphs """
        pdf_name = pdf_path.split("/")[-1]
        chunks_of_text = PDF2Text.pdf_to_string(pdf_path)
        cleaned_text = Cleaner.clean(chunks_of_text)

        # avoiding unexpected behavior by repeating the process
        for _ in range(10):
            try:
                jsonParagraphs = gpt_connector.split_into_paragraphs(cleaned_text).content
                paragraphs_as_list = json.loads(jsonParagraphs)
                pydantic_paragraphs = ParagraphsAdapter.adapt(paragraphs_as_list, pdf_name)
                break
            except Exception as e:
                continue

        # save for debugging purposes
        with open(os.path.join(RESOURCES_LOCATION, "pippo.csv"), "w") as f:
            for p in pydantic_paragraphs:
                row = str(p) + "\n"
                f.write(row)

        chromadb.create_collection(collection_name=pdf_name)
        chromadb.add_paragraphs(collection_name=pdf_name, paragraphs=pydantic_paragraphs)


