class Person:
    def __init__(self):
        self.__id = "hello"
class Student(Person):
    def __init__(self):
        super().__init__()
        print(self._Person__id)

print(Student())

data = {"name":"sarvesh"}

print(data["age"])