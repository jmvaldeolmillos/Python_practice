from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional


class BaseTodo(BaseModel):
    task: str


class Todo(BaseModel):
    id: Optional[int] = None
    task: str
    is_completed: bool = False


class ReturnTodo(BaseTodo):
    pass


app = FastAPI()
todos = []


@app.post("/todos", response_model=ReturnTodo)
async def add_todos(todo: Todo):
    todo.id = len(todos) + 1
    todos.append(todo)
    return todo


@app.get("/todos")
async def read_todos():
    return todos


@app.get("/todos/{id}")
async def read_todos(id: int):
    for todo in todos:
        if todo.id == id:
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")


@app.put("/todos/{id}")
async def update_todo(id: int, new_todo: Todo):
    for index, todo in enumerate(todos):
        if todo.id == id:
            todos[index] = new_todo
            todos[index].id = id
            return
    raise HTTPException(status_code=404, detail="Todo not found")


@app.delete("/todos/{id}")
async def delete_todos(id: int):
    for index, todo in enumerate(todos):
        if todo.id == id:
            del todos[index]
            return {"message": "Todo deleted successfully"}
    raise HTTPException(status_code=404, detail="Todo not found")
