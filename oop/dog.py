from animal import Animal

#subclass of animal
class Dog(Animal):

    def speak(self):
        print(self._name + ": Woof!")
