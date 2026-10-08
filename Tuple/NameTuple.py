#nametuple

from collections import namedtuple
Employee=namedtuple(
"Employee",
["id","name","role"]
)

employee = Employee(1, "John", "Developer")


print(employee.id)
print(employee.name)
print(employee.role)

