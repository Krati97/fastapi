A simple Todo App built with FastAPI. This project demonstrates how to create a basic REST API for managing a list of todos. It includes functionality for adding, reading, updating, and deleting todos.

Features
	•	Create a Todo: Add a new task to the list.
	•	Read Todos: Retrieve all tasks or filter by completion status.
	•	Read a Specific Todo: Fetch a task by its unique ID.
	•	Update a Todo: Modify a task’s details.
	•	Delete a Todo: Remove a task from the list.
	•	Middleware to log request processing times.

Installation and Setup

Follow the steps below to set up the project locally:

Prerequisites
	•	Python 3.7 or above
	•	pip (Python package installer)
	•	Git (optional, for cloning)

Step 1: Clone the Repository
Step 2: Install Dependencies
     Install the required Python packages: 'pip install fastapi pydantic uvicorn'
Step 3: Run the Application
      uvicorn app:app --host 127.0.0.1 --port 5566 --reload    

API Endpoints:
Method	Endpoint	Description
POST	/todos	Add a new todo task.
GET	/todos	Retrieve all todos or filter by completed.
GET	/todos/{id}	Retrieve a specific todo by its id.
PUT	/todos/{id}	Update an existing todo.
DELETE	/todos/{id}	Delete a todo by its id.

Resources
	•	FastAPI Documentation
	•	Pydantic Documentation
	•	Uvicorn Documentation


Happy Coding! 🚀