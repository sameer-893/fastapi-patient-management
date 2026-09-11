from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Patient(BaseModel):
    name: str
    age: int
    email: str


@app.post("/patients")
def create_patient(patient: Patient):
    return patient