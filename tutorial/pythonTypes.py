# Type checking in python

def add(firstName: str | list[int], lastName: str):
    if isinstance(firstName, str):
        return f"{firstName.upper()} {lastName}"
    else:
        return f"{firstName[0]} {firstName[1]} {lastName}"


print(add("John", "Doe"))
