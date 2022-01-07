helloworld = "hello" + " " + "world"
print(helloworld)

repeating = "ilya" * 10
print(repeating)

mylist = [1,2,3]
print("A list: %s" % mylist)

data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."

print(format_string % data)

astring = "Hello world!"
print(astring[-1])

astring = "Hello world!"
print(len(astring[3:7:2])) # should be 2

astring = "Hello world!"
afewwords = astring.split(" ")
print(afewwords)