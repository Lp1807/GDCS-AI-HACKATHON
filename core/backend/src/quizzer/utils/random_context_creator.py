import logging
import random

from chromadb import GetResult

from consts import PARAGRAPHS_PER_PAGE
from database.vectordb import ChromaDB


logger = logging.getLogger(__name__)


class RandomContextCreator:
    def __init__(self, chromadb: ChromaDB):
        self.chroma_db = chromadb

    def create_random_context(self, collection_name: str, max_paragraphs: int = 10) -> (str, list[str]):
        """
        Returns:
            - context: concatenated strings
            - list of document IDs used to create context
        """
        collection = self.chroma_db.get_collection(collection_name)
        tot_paragraphs = collection.count()
        logger.debug(f"tot_paragraphs: {tot_paragraphs}")

        tot_pages = (tot_paragraphs // PARAGRAPHS_PER_PAGE) + 1
        logger.debug(f"tot_pages: {tot_pages}")
        random_page = random.randint(1, tot_pages)
        cluster: GetResult = collection.get(where={"page": str(random_page)})
        paragraphs = cluster["documents"]
        ids = cluster["ids"]
        num_paragraphs = len(paragraphs)
        tot_paragraphs = min(max_paragraphs, num_paragraphs)

        paragraphs = paragraphs[:tot_paragraphs]
        context = ". ".join(paragraphs)

        return context, ids
