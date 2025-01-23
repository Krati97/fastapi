# FastAPI Todo App

A simple **Todo App** built with [FastAPI](https://fastapi.tiangolo.com/). This project demonstrates how to create a basic REST API for managing a list of todos. It includes functionality for adding, reading, updating, and deleting todos.

---

## Features

- **Create a Todo**: Add a new task to the list.  
- **Read Todos**: Retrieve all tasks or filter by completion status.  
- **Read a Specific Todo**: Fetch a task by its unique ID.  
- **Update a Todo**: Modify a task’s details.  
- **Delete a Todo**: Remove a task from the list.  
- **Middleware**: Log request processing times.

---

## Installation and Setup

Follow the steps below to set up the project locally:

### Prerequisites

- **Python 3.7** or above  
- **pip** (Python package installer)  
- **Git** (optional, for cloning)  

---

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/fastapi-todo-app.git
cd fastapi

### Step 2: Install Dependencies

```bash
pip install fastapi pydantic uvicorn

### Step 3: Run the Application

```bash
uvicorn app:app --host 127.0.0.1 --port 5566 --reload

# API Endpoints

| **Method** | **Endpoint**     | **Description**                              |
|------------|------------------|----------------------------------------------|
| `POST`     | `/todos`         | Add a new todo task.                         |
| `GET`      | `/todos`         | Retrieve all todos or filter by `completed`. |
| `GET`      | `/todos/{id}`    | Retrieve a specific todo by its `id`.        |
| `PUT`      | `/todos/{id}`    | Update an existing todo.                     |
| `DELETE`   | `/todos/{id}`    | Delete a todo by its `id`.                   |

# Resources
	•	FastAPI Documentation
	•	Pydantic Documentation
	•	Uvicorn Documentation
