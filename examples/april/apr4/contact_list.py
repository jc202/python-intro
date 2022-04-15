from person import Person

friend = Person("Sandra", "White", "803-454-6677")
friend.display()

friend2 = Person("Bobby", "White", "803-454-6789")
friend2.display()

people = (
    Person("Bobby", "White", "803-454-6789"),
    Person("Kimmy", "White", "803-454-6789"),
    Person("Whitney", "White", "803-454-6789"),
    Person("Dwayne", "White", "803-454-6789"),
)

for person in people:
    person.display()