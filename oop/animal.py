class Animal:

    # Constructor method that initializes the class object with a name attribute
    def __init__(self, name, age, character):
        self._name = name               #protected
        self.__age = age                #private
        self.character = character        #public

    def speak(self):
        pass

    def age(self):
        return self.__age

    def describe(self):
        print("Description......")
        print("name = " + self._name)
        print("age = " , self.__age)

