import os
from pathlib import Path


list_of_files = [
    ".github/workflows/.gitkeep",
    "app/__init__.py",
    "app/main.py",
    "app/config.py",
    "app/agents/__init__.py",
    "app/agents/researcher.py",
    "app/agents/writer.py",
    "app/agents/editor.py",
    "app/tools/__init__.py",
    "app/tools/search_engine.py",
    "app/tasks/__init__.py",
    "app/tasks/generate_ebook.py",
    "app/logger/__init__.py",
    "app/logger/logger.py",
    "app/exception/__init__.py",
    "app/exception/exception.py",
    "app/utils/__init__.py",
    "app/utils/pdf_generator.py",
    "requirements.txt",
    ".gitignore",
    ".dockerignore",
    "README.md",
    "Dockerfile",
    "setup.py",
    "pyproject.toml",
    "setup.cfg",
    "tox.ini",
    "docker-compose.yml",
    ".env",
    "example.env",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        # logging.info(f"Creating directory: {filedir} for file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass