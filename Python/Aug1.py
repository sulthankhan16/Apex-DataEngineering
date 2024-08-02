'''
class NotEligibleError(Exception):
    def __init__(self,age):
        self.age=age
        self.msg="Age must be above 18"
        super().__init__(self.msg)
   



def check_age(age):
    if age<18:
        raise NotEligibleError(age)
    else:
        print('Eligible')

try:
    check_age(11)
except NotEligibleError as n:
    print("Not Eligible and age is ",n.age,n.msg)

'''

#Lambda - Anonymous

# lambda parameters : result/return

'''
Map :
lst=[1,2,3,4,5,6,7,8,9,10]

def multiply(m):
    return m*7

result=tuple(map(multiply,lst))
print(result)


'''

'''
from functools import reduce

lst1=[1,2,3,4]
res=reduce(lambda a,b:a*b,lst1)

print(res)




lst1=list(map(int,input().split(',')))

print(lst1)




age=[18,56,23,7,12,45,89]



res=filter(lambda n: n<18,age)
print(list(res))



names=['Sam','John','Peter']
per=[91,54,78]
classs=['A','B','C']

print(list(zip(names,per,classs)))

'''

names=['Sam','John','Peter','Nick','Steve','Peter']

new_lst=[i for i in names if i!='Peter']
print(new_lst)

#Syntax : new_lst=[i for i in iterable if condition is true]

'''
for i in names:
    if i!="Peter":
        newlst.append(i)
'''


        