# Sebuah kelas sederhana untuk mempresentasikan manusia
class Human:
    def __init__(self, name: str, age: int) -> None:
        if not isinstance(name, str):
            raise TypeError(f"Error, expected the first argument attribute value to a str! Got {type(name).__name__}.")
        self.name = name

        if not isinstance(age, int):
            raise TypeError(f"Error, expected the second argument attribute value to an int! Got {type(name).__name__}.")
        self.age = age

    def __str__(self) -> str:
        return f"{self.name} is {self.age} years old."
    
    def __repr__(self) -> str:
        return f"{type(self).__name__}('{self.name}', {self.age})"

    def greet(self, other) -> str:
        return f"{self.name} greets {other.name}"
    
    def is_adult(self) -> bool:
        """A method to determine wheter the human is an adult or not."""
        return self.human_is_adult(self.age)
    
    @staticmethod
    def human_is_adult(persons_age: int) -> bool:
        """A static method to calculate human adulthood ages."""
        return persons_age > 18
