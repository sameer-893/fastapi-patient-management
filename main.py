from fastapi import FastAPI, Path, Query
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal
import json
app = FastAPI()

class Patient(BaseModel):

    id: Annotated[str, Field(...,description='ID of patient',examples=['P001'])]
    name: Annotated[str, Field(...,description='Name of the Patient')]
    city: Annotated[str, Field(...,description='City where Patient live')]
    age: Annotated[int, Field(...,description='Age of the Patient')]
    gender: Annotated[Literal['male','female'],Field(...,description='gender of patient')]
    height: Annotated[float,Field(...,gt=0,description='Height of the patient in mtrs')]
    weight: Annotated[float,Field(...,gt=0,description='Weight of the patient in kgs')]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = self.weight/(self.height**2)
        return bmi


def load_data():
    with open('patients.json','r') as f:
        data = json.load(f)

    return data

@app.get("/")
def hello():
    return {'message':'Patient Management System'}

@app.get("/about")
def about():
    return{'message': 'A fully functional API to manage your patient records'}

@app.get("/view")
def view():
    data = load_data()
    return data

@app.get('/patient/{patient_id}')
def view_patient(patient_id: str = Path(..., description='ID of patients',example='P002')):
    #load all patient

    data = load_data()

    if patient_id in data:
        return data[patient_id]
    return {'error':'patient not found'}

@app.get("/search")
def search_patient(city:str = Query(..., description="Patient city")):
    data = load_data()

    result = {}

    for patient_id, patient in data.items():
        if patient["city"].lower() == city.lower():
            result[patient_id] = patient

    return result




