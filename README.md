# FastAPI Patient Management API

A simple and practical RESTful Patient Management API built with FastAPI and Pydantic.

This project demonstrates API development with FastAPI, request validation using Pydantic models, patient record management, city-based searching, and BMI calculation using computed fields.

##  Features
📋 View all patient records
👤 View a specific patient by ID
🔍 Search patients by city
✅ Validate patient data with Pydantic
⚖️ Calculate BMI using Pydantic computed fields
📚 Automatic interactive API documentation
⚡ Fast and lightweight REST API
🐍 Built with Python
🛠️ Technologies Used
Python
FastAPI
Pydantic
Uvicorn
JSON

## Project Structure
fastapi-patient-management/
│
├── main.py
├── Pydantic_model.py
├── patients.json
├── requirements.txt
├── .gitignore
└── README.md

## Installation
1. Clone the Repository
git clone https://github.com/sameer-893/fastapi-patient-management.git

2. Navigate to the Project
cd fastapi-patient-management

3. Create a Virtual Environment
python -m venv venv

4. Activate the Virtual Environment

## Windows:

venv\Scripts\activate


## macOS / Linux:

source venv/bin/activate

Install Dependencies
pip install -r requirements.txt

## Run the Application

Start the FastAPI development server:

uvicorn main:app --reload


The API will be available at:

http://127.0.0.1:8000

## API Documentation

FastAPI automatically generates interactive API documentation.

Swagger UI
http://127.0.0.1:8000/docs

ReDoc
http://127.0.0.1:8000/redoc

## API Endpoints
Method	Endpoint	Description
GET	/	Returns a welcome message
GET	/about	Returns API information
GET	/view	View all patients
GET	/patient/{patient_id}	View a patient by ID
GET	/search?city={city}	Search patients by city
POST	/patients	Create a new patient

## Example Requests
Get Patient by ID
GET /patient/P002

Search Patients by City
GET /search?city=Lahore

Create a Patient
POST /patients
Content-Type: application/json

## BMI Calculation

The project uses Pydantic's computed_field to calculate BMI based on the patient's height and weight.

@computed_field
@property
def bmi(self) -> float:
    return self.weight / (self.height ** 2)

## Future Improvements
 Implement complete CRUD operations
 Add database integration
 Add authentication and authorization
 Add pagination
 Add automated tests
 Add Docker support
 Add proper error handling
 Deploy the API to a cloud platform
 


GitHub: @sameer-893

⭐ If you find this project useful, feel free to star the repository!
