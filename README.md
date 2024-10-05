## ebook-generator-ai-agent

### Project Overview

ebook-generator-ai-agent is an AI-powered application designed to generate full eBooks based on a given topic. The project incorporates three intelligent agents that collaboratively produce an eBook:

Researcher Agent: Gathers information and generates the structure (chapters) relevant to the specified topic.

Writer Agent: Writes the content for each chapter based on the research.

Editor Agent: Corrects grammatical mistakes and enhances the content for clarity and readability.

With just an API request specifying the eBook's topic, this system can generate a complete eBook, handling everything from research to final edits.

### Getting Started
#### Prerequisites
Ensure you have the following installed:

Docker: To run the application in a containerized environment.

#### Environment Variables

The following environment variables need to be configured in your .env file:

```
GROQ_API_KEY=<Your_Groq_API_Key>
CELERY_BROKER_URL=<Your_Celery_Broker_URL>
ELASTICSEARCH_HOST=<Your_Elasticsearch_Host>
ELASTICSEARCH_PORT=<Your_Elasticsearch_Port>
ELASTICSEARCH_SCHEME=<Your_Elasticsearch_Scheme>
```

### How to Run

To start the application, run the following command in the project root directory:
```
docker-compose up
```

### API Usage

Create ebook: To generate an eBook, send a POST request to the following endpoint:

```
POST : http://0.0.0.0:8000/generate-ebook/

Request body:

{
  "topic": "Python"
}

```

### Agents Workflow

1. Researcher Agent: Upon receiving the eBook request, this agent performs research on the given topic and identifies key chapters and sections.

2. Writer Agent: Based on the chapters provided by the Researcher, the Writer agent composes the content for each chapter.

3. Editor Agent: Once the content is written, the Editor agent corrects any grammatical errors and refines the text to ensure high-quality output.


### Technologies Used
Python: Core programming language for application logic.

FastAPI: Framework used to develop the API.

Celery: Task queue used to manage asynchronous task execution.

Docker: Containerization tool to ensure easy deployment and consistent environments.

Groq API: Used for AI-based research and content generation.

RabbitMQ: Message broker to handle communication between Celery workers.

FPDF: Library to generate the final eBook in PDF format.

Elasticsearch: Used for logging.

Langchain: To create and execute agents


###### **You can checkout sample-pdf/ folder to get a sample ebook.
