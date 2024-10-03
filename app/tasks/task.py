from celery import Celery
from app.agents.researcher import ResearcherAgent
from app.exception.exception import CustomException
from app.logger.logger import logging
from app.utils.main_util import generate_pdf
from app.agents.writer import WriterAgent
from app.agents.editor import EditorAgent
from app.config import Settings
import traceback
import sys
import gc

settings = Settings()

celery_app = Celery('tasks', broker=settings.CELERY_BROKER_URL)

@celery_app.task
def generate_ebook_task(topic):
    try:
        # Initialize agents
        logging.info("Initializing agents...")
        researcher = ResearcherAgent()
        writer = WriterAgent()
        editor = EditorAgent()

        # Step 1: Research the topic and get chapter titles
        logging.info("Researching the topic...")
        chapters = researcher.research(topic)

        # Step 2: Write content for each chapter
        logging.info("Writing content for each chapter...")
        written_content = [writer.write(chapter, topic) for chapter in chapters]

        # Step 3: Edit each chapter for grammar and consistency
        logging.info("Editing each chapter for grammar and consistency...")
        final_content = [editor.edit(content) for content in written_content]

        # Step 4: Decoding text to latin-1
        logging.info("Decoding text to latin-1...")
        final_content = [content.encode('latin-1', 'replace').decode('latin-1') for content in final_content]

        # Step 5: Generate PDF with all content
        logging.info("Generating PDF with all content...")
        pdf_file_path = generate_pdf(topic, final_content, chapters)

        # Return PDF file path
        logging.info("Task completed.")

        collected = gc.collect()

        logging.info(f"Garbage collector: collected {collected} objects.")
        return pdf_file_path

    except Exception as e:
        logging.exception(F"Error: {e} | Traceback: {traceback.format_exc()}")
        raise CustomException(e, sys)