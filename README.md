# 🏥 Patient Management System API

A simple RESTful API built using **FastAPI** and **Pydantic** for learning backend development and API creation. This project demonstrates how to create, retrieve, update, delete, and sort patient records using FastAPI endpoints.

## 🚀 Features

* View all patients
* View a specific patient
* Create a new patient
* Update patient information
* Delete a patient
* Sort patients based on different criteria
* About endpoint
* Data validation using Pydantic models
* Interactive API documentation using Swagger UI

---

## 🛠️ Technologies Used

* Python
* FastAPI
* Pydantic
* Uvicorn

---

## 📂 Project Structure

```text
patient-management/
│
├── main.py
├── patients.json
├── requirements.txt
├── README.md
│
├── models/
│   └── patient.py
│
├── routes/
│   └── patient_routes.py
│
└── utils/
    └── helper_functions.py
```

> Note: The structure may vary depending on your implementation.

---

## 📌 API Endpoints

### 1. Home Endpoint

```http
GET /
```

Returns a welcome message.

---

### 2. About Endpoint

```http
GET /about
```

Returns information about the Patient Management API.

---

### 3. View All Patients

```http
GET /patients
```

Returns the complete list of patients.

---

### 4. View Patient

```http
GET /patients/{patient_id}
```

Returns details of a specific patient.

---

### 5. Create Patient

```http
POST /patients
```

Creates a new patient record.

#### Example Request Body

```json
{
  "id": 1,
  "name": "John Doe",
  "age": 30,
  "gender": "Male",
  "city": "New York"
}
```

---

### 6. Update Patient

```http
PUT /patients/{patient_id}
```

Updates an existing patient's information.

---

### 7. Delete Patient

```http
DELETE /patients/{patient_id}
```

Deletes a patient record.

---

### 8. Sort Patients

```http
GET /patients/sort
```

Sorts patient records based on specified parameters such as age, name, etc.

---

## 📖 Pydantic Validation

This project uses **Pydantic** models to:

* Validate incoming request data
* Enforce data types
* Provide automatic error handling
* Generate API schemas automatically

Example:

```python
from pydantic import BaseModel

class Patient(BaseModel):
    id: int
    name: str
    age: int
    gender: str
```

---

## ▶️ Running the Project

### Clone the Repository

```bash
git clone https://github.com/jaybapu02/patient-management.git
cd patient-management
```

### Create Virtual Environment

```bash
python -m venv fastAPI
```

### Activate Virtual Environment

Windows:

```bash
fastAPI\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Start the Server

```bash
uvicorn main:app --reload
```

Server will run at:

```text
http://127.0.0.1:8000
```

---

## 📚 API Documentation

FastAPI automatically generates API documentation.

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

### ReDoc

```text
http://127.0.0.1:8000/redoc
```

---

## 🎯 Learning Objectives

This project helped in understanding:

* FastAPI fundamentals
* REST API development
* CRUD operations
* Path and Query Parameters
* Pydantic Models
* Request Validation
* API Documentation
* JSON Data Handling

---

## 🔮 Future Improvements

* Database integration (MySQL/PostgreSQL)
* Authentication and Authorization
* JWT Token-based Security
* Pagination
* Search Functionality
* Docker Deployment

---

## 👨‍💻 Author

**Jaychandra Das**

B.Tech (CSE - AI) Student
Gandhi Institute For Technology (GIFT Autonomous)

Learning FastAPI, Pydantic, Machine Learning, and Backend Development.
