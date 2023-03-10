from dataclasses import dataclass


@dataclass
class Person:
    full_name: str = None
    firstname: str = None
    lastname: str = None
    datetime: str = None
    email: str = None
    phone_number: int = None
    age: int = None
    salary: int = None
    department: str = None
    current_address: str = None
    permanent_address: str = None