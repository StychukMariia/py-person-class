class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    result_list = []
    for person in people:
        new_person = Person(person["name"], person["age"])
        result_list.append(new_person)
    for person_p in people:
        if person_p.get("wife") is not None:
            Person.people[person_p["name"]].wife = (
                Person.people)[person_p["wife"]]
        elif person_p.get("husband") is not None:
            Person.people[person_p["name"]].husband = (
                Person.people)[person_p["husband"]]
    return result_list
