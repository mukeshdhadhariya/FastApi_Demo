from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app=FastAPI()

class demo(BaseModel):
    id:int
    name:str
    origin:str

demos:List[demo]=[]

@app.get("/")
def read_demo():
    return {"message":"Welcome to demo"}

@app.get("/demos")
def get_demon():
    return demos

@app.post("/demos")
def add_demo(demo:demo):
    demos.append(demo)
    return demo

@app.put("/demos/{demo_id}")
def update_demo(demo_id:int,updated_demo:demo):
    for index,demo in enumerate(demos):
        if demo.id==demo_id:
            demos[index]=updated_demo
            return updated_demo
        
    return {"error":"demo err accure"}

@app.delete("/demos/{demo_id}")
def delete_demo(demo_id:int):
    for index,demo in enumerate(demos):
        if demo.id==demo_id:
            deleted=demos.pop(index)
            return deleted
    return {"error": "demo err accure"}