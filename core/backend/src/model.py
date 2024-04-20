from pydantic import BaseModel, Field


class ParagraphMetadata(BaseModel):
    pdf_name: str = Field(...,
                          title="Name of the PDF file the paragraph belongs to",
                          example="example.pdf")
    page: str = Field(...,
                      title="Page number the paragraph is located on",
                      example="1")


class Paragraph(BaseModel):
    content: str = Field(...,
                         title="textual content of the paragraph",
                         example="This is an example paragraph.")
    metadata: ParagraphMetadata = Field(...,
                                        title="Metadata of the PDF file",
                                        example={"pdf_name": "example.pdf", "page": 1})



# ----------- ChromaDB Query Result
class IDs(BaseModel):
    # Define the IDs structure here
    pass

class Embedding(BaseModel):
    # Define the Embedding structure here
    pass





class URI(BaseModel):
    # Define the URI structure here
    pass


class Data(BaseModel):
    # Define the Loadable structure here
    pass


class Metadata(BaseModel):
    # Define the Metadata structure here
    pass


class QueryResult(BaseModel):
    ids: list[str] | None
    embeddings: list[list[Embedding]] | None = None
    documents: list[list[str]] | None = None
    uris: list[list[URI]] | None = None
    data: list[Data] | None = None
    metadatas: list[list[dict[str, float | int | str]]] | None = None
    distances: list[list[float]] | None = None
