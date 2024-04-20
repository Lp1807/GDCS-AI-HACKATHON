import fitz
from tqdm import tqdm


class Extractor:
    @staticmethod
    def pdf_to_string(input_pdf_path: str) -> str:
        pdf_doc = fitz.open(input_pdf_path)
        text = ""

        print("Extracting text from PDF...")
        for i in tqdm(range(len(pdf_doc))):
            page = pdf_doc[i]
            text += page.get_text()
        print("Done.")

        pdf_doc.close()
        return text

    @staticmethod
    def pdf_to_txt(input_pdf_path: str, output_txt_path: str) -> None:
        text = Extractor.pdf_to_string(input_pdf_path)
        with open(output_txt_path, "w") as output_txt:
            output_txt.write(text)
