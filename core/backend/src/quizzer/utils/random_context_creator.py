import logging
import random

from chromadb import GetResult

from core.backend.src.vectordb import ChromaDB


logger = logging.getLogger(__name__)


class RandomContextCreator:
    def __init__(self, chromadb: ChromaDB):
        self.chroma_db = chromadb

    def create_random_context(self, collection_name: str, max_paragraphs: int = 10) -> str:
        collection = self.chroma_db.get_collection(collection_name)
        tot_paragraphs = collection.count()
        logger.debug(f"tot_paragraphs: {tot_paragraphs}")

        tot_pages = (tot_paragraphs // 15) + 1
        logger.debug(f"tot_pages: {tot_pages}")
        random_page = random.randint(1, tot_pages)
        cluster: GetResult = collection.get(where={"page": str(random_page)})
        documents = cluster["documents"]
        num_paragraphs = len(documents)
        tot_paragraphs = min(max_paragraphs, num_paragraphs)

        documents = documents[:tot_paragraphs]
        return ". ".join(documents)
