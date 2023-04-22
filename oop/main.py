from cat import Cat
from dog import Dog


animals = [Dog("Rover", 1, "sleepy"), Cat("Whiskers", 2, "active")]

for animal in animals :
    animal.speak()

    print("access protected var --> name = " + animal._name)

    print("access private var --> age = " , animal.age())   #cannot access private var directly; use method

    print("access public var --> age = " , animal.character)

    animal.describe()

    print("\n")