from consts import TEST_PDF_LOCATION, TEST_PDF_SHORT_LOCATION
from paragraphs_extraction_pipeline.paragraphs_extraction_pipeline import ParagraphsExtractionPipeline


if __name__ == "__main__":
    pdf_path = TEST_PDF_SHORT_LOCATION
    ParagraphsExtractionPipeline.run(pdf_path)



