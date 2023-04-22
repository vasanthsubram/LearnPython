from animal import Animal
#subclass of animal
class Cat(Animal):

    def speak(self):
        print(self._name + ": Meow!")