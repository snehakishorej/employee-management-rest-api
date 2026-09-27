from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from .models import Employee, EmployeeCreate, EmployeeUpdate
from .store import employee_store

app = FastAPI(
    title="Employee Management REST API",
    description="CRUD API built with FastAPI and Pydantic.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Employee Management REST API is running"}

@app.get("/employees", response_model=list[Employee])
def get_employees():
    return list(employee_store.values())

@app.get("/employees/{employee_id}", response_model=Employee)
def get_employee(employee_id: int):
    employee = employee_store.get(employee_id)
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee

@app.post("/employees", response_model=Employee, status_code=status.HTTP_201_CREATED)
def create_employee(employee: EmployeeCreate):
    new_id = max(employee_store.keys(), default=0) + 1
    new_employee = Employee(id=new_id, **employee.model_dump())
    employee_store[new_id] = new_employee
    return new_employee

@app.put("/employees/{employee_id}", response_model=Employee)
def replace_employee(employee_id: int, employee: EmployeeCreate):
    if employee_id not in employee_store:
        raise HTTPException(status_code=404, detail="Employee not found")
    updated = Employee(id=employee_id, **employee.model_dump())
    employee_store[employee_id] = updated
    return updated

@app.patch("/employees/{employee_id}", response_model=Employee)
def update_employee(employee_id: int, employee: EmployeeUpdate):
    existing = employee_store.get(employee_id)
    if existing is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    updates = employee.model_dump(exclude_unset=True)
    updated = existing.model_copy(update=updates)
    employee_store[employee_id] = updated
    return updated

@app.delete("/employees/{employee_id}")
def delete_employee(employee_id: int):
    if employee_id not in employee_store:
        raise HTTPException(status_code=404, detail="Employee not found")
    deleted = employee_store.pop(employee_id)
    return {"message": "Employee deleted successfully", "employee": deleted}
