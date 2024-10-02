from fastapi import FastAPI, BackgroundTasks
from app.tasks.task import generate_ebook_task
from app.config import Settings

app = FastAPI()
settings = Settings()

@app.post("/generate-ebook/")
async def generate_ebook(topic: str, background_tasks: BackgroundTasks):
    task = generate_ebook_task.delay(topic)
    return {"message": "Ebook generation started", "task_id": task.id}

@app.get("/ebook-status/{task_id}")
async def get_ebook_status(task_id: str):
    task = generate_ebook_task.AsyncResult(task_id)
    if task.state == 'PENDING':
        return {"status": "Pending"}
    elif task.state == 'SUCCESS':
        return {"status": "Task Completed", "pdf_link": task.result}
    elif task.state == 'FAILURE':
        return {"status": "Task failed"}
    else:
        return {"status": task.state}