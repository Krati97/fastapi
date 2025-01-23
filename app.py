
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from time import time
from fastapi.middleware.cors import CORSMiddleware

class BaseTodo(BaseModel):
    task: str
    
class Todo(BaseTodo):
    id: Optional[int] = None
    is_completed: bool = False

class ReturnTodo(BaseTodo):
    pass

app = FastAPI()

todos = []

@app.middleware("http")
async def log_middleware(request, call_next):
    start_time = time()
    response = await call_next(request)
    end_time = time()
    process_time = end_time - start_time
    print(f"Request {request.url} processed in {process_time} sec")
    return response
    

@app.post("/todos", response_model=ReturnTodo)
async def add_todos(todo: Todo):
    todo.id = len(todos) + 1
    todos.append(todo)
    return todo


@app.get("/todos")
async def read_todos(completed: Optional[bool] = None):
    if completed is None:
        return todos
    else:
        return [todo for todo in todos if todo.is_completed == completed]

@app.get("/todos/{id}")
async def read_todo(id: int):
    for todo in todos:
        if todo.id == id:
            return todo
    raise HTTPException(status_code=404, detail="Not found")    
        
        
@app.put('/todos/{id}')
async def update_todo(id: int, new_todo: Todo):
    for index, todo in enumerate(todos):
        if todo.id == id:
           todos[index]  = new_todo
           todos[index].id = id
           return 
    raise HTTPException(status_code=404, detail="Not found")    


@app.delete('/todos/{id}')
async def delete_todo(id: int):
    for index, todo in enumerate(todos):
        if todo.id == id:
            del todos[index]
            return
    raise HTTPException(status_code=404, detail="Not found")    
