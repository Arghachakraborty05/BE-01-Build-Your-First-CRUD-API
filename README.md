\# Task API



A small in-memory CRUD API built with Python and FastAPI as part of the FlyRank Backend AI Engineering assignment (BE-01).



\## Features



\* Create tasks

\* Read all tasks or a single task

\* Update a task title and/or completion status

\* Delete tasks

\* Input validation and 404 error handling

\* Interactive Swagger UI documentation

\* In-memory task storage



\## Requirements



\* Python 3.10+

\* FastAPI

\* Uvicorn



\## Run locally



Install the dependencies:



```bash

pip install -r requirements.txt


```



Start the API server:



```bash

python -m uvicorn main:app --reload

```



The API will run at:



`http://localhost:8000`



Swagger UI is available at:



`http://localhost:8000/docs`



\## API Endpoints



| Method | Endpoint           | Description                                 |

| ------ | ------------------ | ------------------------------------------- |

| GET    | `/`                | Get API information and available endpoints |

| GET    | `/health`          | Check whether the API is running            |

| GET    | `/tasks`           | Get all tasks                               |

| POST   | `/tasks`           | Create a new task                           |

| GET    | `/tasks/{task\\\_id}` | Get a single task by ID                     |

| PUT    | `/tasks/{task\\\_id}` | Update a task by ID                         |

| DELETE | `/tasks/{task\\\_id}` | Delete a task by ID                         |



\## Example Request



\### Create a task



```powershell

$body = '{"title":"Buy milk"}'; $body | curl.exe -i -X POST http://localhost:8000/tasks -H "Content-Type: application/json" --data-binary "@-"

```

Example response:

```text

HTTP/1.1 201 Created

content-type: application/json



{"id":4,"title":"Buy milk","done":false}

```



\## Swagger UI



The API uses FastAPI's built-in Swagger UI for interactive API documentation and testing.



Open:



`http://localhost:8000/docs`



!\[Swagger UI](screenshots/swagger-ui.png)



\## Data Storage



Tasks are stored in memory only. No database or external file storage is used.



The initial task list contains three example tasks. Because the data is stored in memory, changes are reset when the application restarts.



\## Project Structure



```text

BE-01-Build-Your-First-CRUD-API/

├── main.py

├── requirements.txt

├── .gitignore

├── README.md

└── screenshots/

      └── swagger-ui.png

```

