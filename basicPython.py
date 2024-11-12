print("Hello Python")

myInt = 5
print(myInt)

myFloat = 7.0
print(myFloat)

myFloat = float(8)
print(myFloat)

myString = "Hello "
print(myString)

myString = 'World'
print(myString)

one = 1
two = 2
three = one + two
print(three)

hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)

a, b = 3,4
print(a,b)

#print number and string
name = "John"
age = 30
#using concatnation
print('using concatenation')
print("My name is " + name + " and I am " + str(age) + " years old.")

#using f string
print("using f string")
print(f"My name is {name} and I am {age} years old.")

#using formatted string
print("using formatted string")
message = "My name is {} and I am {} years old."
formatted_message = message.format(name, age)
print(formatted_message)

#using join()
print("using join")
print("My name is", name, "and I am", age, "years old.")