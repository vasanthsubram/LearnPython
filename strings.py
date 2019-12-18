name = "vasanth"
print("Hello, " , name)

print("Hello, %s " % name)

age = 23
print("%s is %d years old" %(name,age))


#Any object which is not a string can be formatted using the %s operator as well.
# The string which returns from the "repr" method of that object is formatted as the string
list = [1,2,3]
print("list = %s" %list)

# %s - String (or any object with a string representation, like numbers)
# %d - Integers
# %f - Floating point numbers
# %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
# %x/%X - Integers in hex representation (lowercase/uppercase)

string = "HelloWorld"
print(len(string))
print(string.index('o'))

# This counts the number of l's in the string
print(string.count('l'))

###Range - the end index is not included
# This prints a slice of the string, starting at index 6, and ending at index 9.
print(string[6:9])  #orl

#prints 4th character from the end to the 1st character from the end
print(string[-4:-1])   #orl

#skip 1 (same result as no skipping)
print(string[1:7])      #elloWo
print(string[1:7:1])    #elloWo

#skip 2
print(string[1:7:2])    #elW

#reverse string using skipping
print(string[::-1])

print(string.upper())
print(string.lower())

#starts or ends with some string
print(string.startswith("Hell"))
print(string.endswith("Hell"))

#split string (returs array)
print("Hello World".split(" "))