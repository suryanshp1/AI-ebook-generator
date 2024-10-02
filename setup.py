from setuptools import find_packages, setup

setup(
    name="ebook-generator",
    version="0.0.1",
    author="Suraj",
    author_email="suryanshp1@gmail.com",
    install_requires=["fastapi", "uvicorn", "langchain", "celery", "langchain-community", "langchain_groq", "rabbitmq-client", "requests", "flower", "pydantic-settings", "fpdf2", "duckduckgo-search"],
    packages=find_packages(),
)