from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI(title="Task API", version="1.0")

tasks = [
    {"id": 1, "title": "Learn FastAPI", "done": False},
    {"id": 2, "title": "Build CRUD API", "done": False},
    {"id": 3, "title": "Test the API", "done": False},
]

@app.get("/", description="Get API information and available endpoints.")
def root():
    return {
        "name": "Task API",
        "version": "1.0",
        "endpoints": ["/tasks"]
    }


@app.get("/health", description="Check whether the API is running.")
def health():
    return {"status": "ok"}

@app.get("/tasks", description="Get all tasks.")
def get_tasks():
    return tasks

@app.get("/tasks/{task_id}", description="Get a single task by ID.")
def get_task(task_id: int):
    task = next((task for task in tasks if task["id"] == task_id), None)

    if task is None:
        return JSONResponse(
            status_code=404,
            content={"error": f"Task {task_id} not found"}
        )

    return task

@app.post("/tasks", status_code=201, description="Create a new task.")
def create_task(task_data: dict):
    title = task_data.get("title")

    if not isinstance(title, str) or not title.strip():
        return JSONResponse(
            status_code=400,
            content={"error": "Title is required"}
        )

    new_id = max(task["id"] for task in tasks) + 1

    new_task = {
        "id": new_id,
        "title": title.strip(),
        "done": False
    }

    tasks.append(new_task)

    return new_task

@app.put("/tasks/{task_id}", description="Update a task by ID.")
def update_task(task_id: int, task_data: dict):
    task = next((task for task in tasks if task["id"] == task_id), None)

    if task is None:
        return JSONResponse(
            status_code=404,
            content={"error": f"Task {task_id} not found"}
        )

    if not task_data:
        return JSONResponse(
            status_code=400,
            content={"error": "Request body cannot be empty"}
        )

    if "title" in task_data:
        title = task_data["title"]

        if not isinstance(title, str) or not title.strip():
            return JSONResponse(
                status_code=400,
                content={"error": "Title must be a non-empty string"}
            )

        task["title"] = title.strip()

    if "done" in task_data:
        done = task_data["done"]

        if not isinstance(done, bool):
            return JSONResponse(
                status_code=400,
                content={"error": "Done must be a boolean"}
            )

        task["done"] = done

    if "title" not in task_data and "done" not in task_data:
        return JSONResponse(
            status_code=400,
            content={"error": "At least one of title or done is required"}
        )

    return task

@app.delete("/tasks/{task_id}", status_code=204, description="Delete a task by ID.")
def delete_task(task_id: int):
    task = next((task for task in tasks if task["id"] == task_id), None)

    if task is None:
        return JSONResponse(
            status_code=404,
            content={"error": f"Task {task_id} not found"}
        )

    tasks.remove(task)