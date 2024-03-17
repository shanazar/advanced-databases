
class Student:

    def __init__(self, num_id: int, name: str, age: int, gender: str, city: str):
        self.num_id = int(num_id)
        self.name = name
        self.age = age
        self.gender = gender
        self.city = city

    def set_name(self, name: str) -> None:
        self.name = name

    def set_age(self, age: int) -> None:
        self.age = age

    def set_gender(self, gender: str) -> None:
        self.gender = gender

    def set_city(self, city: str) -> None:
        self.city = city

    def get_id(self) -> int:
        return self.num_id

    def get_name(self) -> str:
        return self.name

    def get_age(self) -> int:
        return self.age

    def get_gender(self) -> str:
        return self.gender

    def get_city(self) -> str:
        return self.city

    def __str__(self):
        return f"{self.num_id}"

    def __repr__(self):
        return f"{self.num_id}"
