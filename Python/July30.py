#Control Flow Statements:

# If - Else Statment
'''
age =int(input())

if age>0 and age<18:
    print('Child')
elif age>=18 and age<=59:
    print('Adult')
else:
    print('Senior Citizen')
    if age>70:
        print('Lower Bearth')
    else:
        print('User Choice')

'''

'''
if condition

else () {

}

age =int(input())
if age<18:
    print('Child')
elif age>=18 and age<=59:
    print('Adult')
else:
    print('Senior Citizen')




for i in range(1,11,1): #1 to 10 is range
    print(i*3)

    

fruits=['Apple','Banana','Strawberry','Kiwi']

for i in range(len(fruits)):
    print(fruits[i])


i=0
while i<11: # false
    print(i) #1
    i=i+1 #i=11



def areaofcircle(radius):
    area= 3.14*(radius**2)
    print('Area is ',area)

radius = int(input())
areaofcircle(radius)



def areaofrectangle(length,breadth=4):
    print('Area of rectangle',length*breadth)
    print('Length is',length)
    print('Breadth is',breadth)

#breadth value is default = 4
# User to give input of length
areaofrectangle(3,5)

'''

#Costructor is invoked Automatically when object is created. __int__
class Car:
    def __init__(self):
        print('Neutral Gear')

    def move(self,speed):
        print('Moving...')
        self.speed=speed
        print('Speed is',self.speed)
        self.gear=4
    def reverse(self):
        print("Reverse...")
        print('Speed is',self.speed)
        print("number of gears",self.gear)

    def stop():
        print('Braking...')

c = Car() #created object
c.move(56)
c.reverse()