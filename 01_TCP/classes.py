class _User:
    first_name: str
    last_name: str

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def full_name(self):
        return f"Fullname is: {self.first_name} {self.last_name}, age is {self.age}"

class AgedUser(_User):
    age: int

    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name)
        self.age = age




john = AgedUser('John', 'Doe', 30)
print(john.full_name())