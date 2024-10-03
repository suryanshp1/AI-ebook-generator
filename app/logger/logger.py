import logging
import os
from datetime import datetime
from app.config import Settings
from elasticsearch import Elasticsearch

settings = Settings()

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# Set up Elasticsearch client
es = Elasticsearch([{'host': settings.ELASTICSEARCH_HOST, 'port': int(settings.ELASTICSEARCH_PORT), 'scheme': settings.ELASTICSEARCH_SCHEME}])

# Custom Elasticsearch log handler
class ElasticsearchHandler(logging.Handler):
    def emit(self, record):
        doc = {
            'message': record.getMessage(),
            'level': record.levelname,
            'logger': record.name
        }
        es.index(index="ebook-generator-logs", body=doc)