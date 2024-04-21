import json
import logging
from pathlib import Path

from fastapi import UploadFile, File
from starlette.responses import JSONResponse

from connectors import chromadb, gpt_connector
from consts import GENERATED_QUIZ_LOCATION, UPLOADED_PDFS_DIRECTORY
from main import app
from paragraphs_extraction_pipeline.paragraphs_extraction_pipeline import ParagraphsExtractionPipeline
from quizzer.quizzer import Quizzer

logger = logging.getLogger(__name__)


@app.get("/startquiz")
def read_quiz():
    with open(GENERATED_QUIZ_LOCATION, "r") as quiz:
        return json.loads(quiz.read())


@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    try:
        # Get the file contents
        contents = await file.read()
        print(contents)
        # Create the file path
        file_path = Path(UPLOADED_PDFS_DIRECTORY) / file.filename

        # Write the file to the specified file path
        with open(file_path, "wb") as f:
            f.write(contents)
        logger.info("Starting pipeline...")
        ParagraphsExtractionPipeline.run(str(file_path))
        quizzer = Quizzer(chromadb, gpt_connector)
        pdf_name = str(file_path).split("/")[-1]
        quizzer.generate_and_save_quiz(pdf_name=pdf_name)

        # Return success message
        return JSONResponse(content={"message": "File uploaded successfully and quiz created.", "file_path": str(file_path)})
    except Exception as e:
        # Return error message if something goes wrong
        logger.error(e)
        return JSONResponse(content={"error": str(e)}, status_code=500)