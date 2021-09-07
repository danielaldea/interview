# Send your code in *.py extension and the code should be runnable .Tests will be appreciated as well
# Please keep in mind that each exercises will get scores for different implementations (so many , so good)

# 1.	Create a dictionary of names from two lists:  indexes in range 0..5 and list of 5 names

l_index = [0,1,2,3,4,5]
l_names = ['Alex', 'Daniel', 'Dragos', 'Andreea', 'Mihai', 'Catalin']

d = {}
a_string = "-" * 107

for name in l_names:
    for index in l_index:
        d[index] = name
        l_index.remove(index)
        break

print('The dictionary is:' + str(d))

print(a_string)

# 2.	For a given dictionary change the switch the k,v in v,k
#  Example: {0: 'alex', 1: 'ada', 2: 'teddy',
#             3: 'bob', 4: 'cristian', 5: 'marry'}
#  Becomes: {'alex':0, 'ada':1, 'teddy': 2...}

new_d = {}
for l_index, l_names in d.items():
    new_d[l_names] = l_index

print('Dictonary change the swich:' + str(new_d))

print(a_string)

# 3.	Remove each element in interval [start_interval, end_interval) from a_list and calculate the sum of removed elements.
# Example:
# Given a list, 5, 10, 15, 20, 25, if elements in interval [0,2) are removed, the list will containt 15, 20, 25 and the sum of elements is 15.
# Complete the following funtion:
def replace():
    total = 0
    a_list = [3, 6, 9, 12, 15]
    print("This is the list:" + str(a_list))
    new_list = list(a_list[0:2])
    print("This is a list of elem in the range [0:2]:" + str(new_list))
    for elem in range(0, len(new_list)):
        total = total + new_list[elem]
    print("The sum of the elements is:" + str(total))

print(replace())
print(a_string)

# 4. a.Given class Bird, write the code that will output in the console
#  	the message:"initialize Bird class"
#  b.Using Pigeon class and updating the code you will get the same output
# (It’s enough one solution)

class Bird():
    def __init__(self):
        print("initialize Bird class")
    def fly(self):
        print("Bird can fly")

class Pigeon(Bird):
    def __init__(self):
        print("initialize Pigeon child class")
    def fly(self):
        super().fly()

bird = Bird()
bird.fly()
print(a_string)
pigeon = Pigeon()
pigeon.fly()
