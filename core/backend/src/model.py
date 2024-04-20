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


