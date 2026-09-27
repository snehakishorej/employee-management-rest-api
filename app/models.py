from pydantic import BaseModel, Field

class EmployeeBase(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    age: int = Field(ge=18, le=100)
    role: str = Field(min_length=2, max_length=100)
    salary: float = Field(gt=0)

class EmployeeCreate(EmployeeBase):
    pass

class EmployeeUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=2, max_length=100)
    age: int | None = Field(default=None, ge=18, le=100)
    role: str | None = Field(default=None, min_length=2, max_length=100)
    salary: float | None = Field(default=None, gt=0)

class Employee(EmployeeBase):
    id: int
