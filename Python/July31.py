'''

Map - 


def double(n):
    return n * 2


numbers = [5, 6, 7, 8]
result = map(double, numbers)
print(list(result))
Reduce -
import functools


numbers = [1, 2, 3, 4]

# Use reduce to compute the product of list elements
product = functools.reduce(lambda x, y: x * y, numbers)
print("Product of list elements:", product)
Filter -
# Define a function to check if a number is even
def is_even(n):
    return n % 2 == 0

# Define a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use filter to filter out even numbers
even_numbers = filter(is_even, numbers)
print("Even numbers:", list(even_numbers))  


'''

'''
#Inheritance:

class Vehicle:

    def four(self):
        print('Four Wheel')


class Car(Vehicle):
    def __init__(self):
        print('Neutral Gear')

    def move(self):
        print('Moving...')
        
    def reverse(self):
        print("Reverse...")

    def stop(self):
        print('Braking...')

class BMW(Car,Vehicle):
    def automatic(self,gears):
        self.gears=gears
        print('Automatic Shift')
        print('Number of gears',gears)
        

    def rooftop(self):
        print('Roof Top')
        print('Number of gears',self.gears)
        
    def power_steering():
        print('Power Steering')

b=BMW()
b.automatic(4)
b.four()


'''
'''
#Polymorphism :

class Vehicle:
    def move():
        print('Moving..Vehicle')
class Car:
    def move():
        print('Moving..Car')

v=Vehicle
v.move()
c=Car
c.move()



try:
    print('Hello')

except:
    print('There is a Error')

print('Hi')


def display():
    try:
        return 'Hello'

    except:
        return 'There is a Error'
    finally:
        print('Byee')

print(display())




import math as mh
mh.sqrt()


#args
def scores(*args):
    print(args[1])

scores(1,2,5,6,3,5,8)



#kwargs
'''

lst1=['Sulthan','Praveen','Himanshu']
lst2=[91,93,97]

def join_fun(**kwargs):
    for i,j in kwargs.items():
        print(i,j)
        

join_fun(name=lst1,per=lst2)

