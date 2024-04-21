from consts import PARAGRAPHS_PER_PAGE
from database.model import Paragraph


class ParagraphsAdapter:
    @staticmethod 
    def adapt(paragraphs_as_list: list[str], pdf_name: str) -> list[Paragraph]:
        count = 0
        page = 1   
        pydantic_paragraphs = []
        for paragraph in paragraphs_as_list:
            if count < PARAGRAPHS_PER_PAGE:
                pydantic_paragraphs.append(Paragraph(content=paragraph, 
                                                 metadata={"pdf_name": pdf_name, "page": str(page)}))
                count += 1
            else:
                count = 0
                page += 1
        
        return pydantic_paragraphs
