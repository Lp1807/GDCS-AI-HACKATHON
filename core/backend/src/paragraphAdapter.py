import json
from model import Paragraph
from gptconnector import GPTConnector


class paragraphAdapter:
    @staticmethod 
    def adapt(paragraphs_as_list: list[str]) -> list[Paragraph]:
        count = 0
        page = 1   
        pydantic_paragraphs = []
        for paragraph in paragraphs_as_list:
            if count < 15:
                pydantic_paragraphs.append(Paragraph(content=paragraph, 
                                                 metadata={"pdf_name": "example.pdf", "page": str(page)}))
                count += 1
            else:
                count = 0
                page += 1
        
        return pydantic_paragraphs
        

