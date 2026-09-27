from .models import Employee

employee_store: dict[int, Employee] = {
    1: Employee(id=1, name="Sneha", age=22, role="Python Developer", salary=50000),
    2: Employee(id=2, name="Rahul", age=24, role="Backend Developer", salary=60000),
}
