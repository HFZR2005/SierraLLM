from typing import List, Dict

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.llm import generate_scenario
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

def parse_text_to_dict(text):
    lines = text.strip().split("\n")
    data = {}

    for line in lines:
        if ": " in line:
            key, value = line.split(": ", 1)  # Split only on the first occurrence
            data[key.strip()] = value.strip()

    return data

@app.get("/generate_scenario")
async def get_scenario():
    return parse_text_to_dict(generate_scenario())


