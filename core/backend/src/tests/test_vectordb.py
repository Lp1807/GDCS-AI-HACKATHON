from unittest import TestCase

from core.backend.src.database.model import Paragraph, ParagraphMetadata
from core.backend.src.database.vectordb import ChromaDB


class TestVectorDb(TestCase):

    def setUp(self) -> None:
        # Setup Vector Database
        self.chroma_db = ChromaDB()
        self.collection_name = "mypdf.pdf"
        self.chroma_db.create_collection(collection_name=self.collection_name)
        paragraphs = [Paragraph(content="Nel mezzo del cammin di nostra vita mi ritrovai per una selva oscura.",
                                metadata=ParagraphMetadata(pdf_name=self.collection_name,
                                                           page="1")),
                      Paragraph(content="Aaaa quanto dir qual era è cosa dura.",
                                metadata=ParagraphMetadata(pdf_name=self.collection_name,
                                                           page="1")),
                      Paragraph(content="Esta selva selvaggia tanto e aspra e forte che nel pensier rinova la paura.",
                                metadata=ParagraphMetadata(pdf_name=self.collection_name,
                                                           page="1")),
                      Paragraph(content="L'inter ha vinto la champions league.",
                                metadata=ParagraphMetadata(pdf_name=self.collection_name,
                                                           page="1"))
                      ]
        self.chroma_db.add_paragraphs(self.collection_name, paragraphs)

    def test_inter(self):

        result = self.chroma_db.query(collection_name=self.collection_name, query="Chi ha vinto la champions?")
        print(result)

    def test_selva(self):
        result = self.chroma_db.query(collection_name=self.collection_name, query="dove mi ritrovai?")
        print(result)


