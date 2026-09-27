# Employee Management REST API

A beginner-friendly REST API built with FastAPI and Pydantic.

## Features
- Create, retrieve, update and delete employees
- PUT and PATCH support
- Pydantic validation
- HTTP status codes
- Swagger/OpenAPI documentation
- CORS configuration

## Setup

```powershell
cd D:\employee-management-rest-api
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload
```

API: http://127.0.0.1:8000

Swagger: http://127.0.0.1:8000/docs

## Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | /employees | Get all employees |
| GET | /employees/{id} | Get one employee |
| POST | /employees | Create employee |
| PUT | /employees/{id} | Replace employee |
| PATCH | /employees/{id} | Partially update employee |
| DELETE | /employees/{id} | Delete employee |

## Example POST body

```json
{
  "name": "Ananya",
  "age": 23,
  "role": "Full Stack Developer",
  "salary": 55000
}
```

## Project flow

Client / Swagger -> HTTP Request -> FastAPI -> Pydantic Validation -> CRUD Logic -> Employee Store -> Response

## Interview explanation

I built an Employee Management REST API using FastAPI. It supports CRUD operations for employee records. I used Pydantic models for request validation, HTTP status codes for clear API responses, CORS middleware for frontend communication, and Swagger/OpenAPI for interactive API documentation.

Note: This learning version uses an in-memory dictionary instead of a database, so data resets when the server restarts.
