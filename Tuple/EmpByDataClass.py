#empby dataclass

from  dataclasses import dataclass
@dataclass
class Employee:
    employee_id:str
    name:str
    role:str
    salary:int
    
    
employee=Employee(
    "Ep101",
    "rahul",
    "developer",
    75000
    )
    
    
print(employee.name)
print(employee.role)
print(employee.salary)