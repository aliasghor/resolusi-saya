# A simple Human class that represents human (e.g., their names, behaviour to greet, and determining if the human is an adult).
class Human:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"{self.name} is {self.age} years old."
    
    def __repr__(self) -> str:
        return f"{type(self).__name__}('{self.name}', {self.age})"

    def greet(self, other) -> str:
        return f"{self.name} greets {other.name}"
