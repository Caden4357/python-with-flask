# 1. TASK: print "Hello World"
from operator import index


print("Hello World")
# 2. print "Hello Noelle!" with the name in a variable
name = "Noelle"
print("Hello", name)
print(f"hello, {name}!")	# with a comma
print("hello " + name)	# with a +
# 3. print "Hello 42!" with the number in a variable
name = 42
print(f"Hello {name}")	# with a comma
# print("Hello " + name)	# with a +	-- this one should give us an error!
# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print("I love to eat {} and {}".format(fave_food1,fave_food2)) # with .format()
print(f"I love to eat {fave_food1} and {fave_food2}") # with an f string


students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterate_dictionary(list):
    for i in range(0, len(list)-1):
        output = ""
        for key,val in list[i].items():
            output += f" {key} - {val},"
        print(output)

iterate_dictionary(students)
