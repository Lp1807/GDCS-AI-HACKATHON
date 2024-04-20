import random

import chromadb

from core.backend.src.model import Paragraph, QueryResult


class ChromaDB:
    """
    https://docs.trychroma.com/reference/Collection
    """

    def __init__(self):
        self.client = chromadb.Client()

    def create_collection(self, collection_name: str):
        self.client.create_collection(collection_name)

    def add_paragraphs(self, collection_name: str, paragraphs: list[Paragraph]):
        collection = self.client.get_collection(collection_name)
        documents = [paragraph.content for paragraph in paragraphs]
        metadatas = [paragraph.metadata.model_dump() for paragraph in paragraphs]
        ids = [str(random.random()*(i+1)*100) for i in range(len(documents))]
        collection.add(documents=documents, metadatas=metadatas, ids=ids)

    def query(self, collection_name: str, query: str) -> str:
        collection = self.client.get_collection(collection_name)
        result: QueryResult = collection.query(query_texts=[query], n_results=2)
        print(result)
        return result["documents"][0][0]
