'''
Need a File

Mode - r,w,a,x

w- override all data

import os

os.remove('sample.txt')

pip install package_name

Copy - The modifications done either to original array or duplicate will not apply to each other
view - If you modify in either of them, the changes will apply to both


'''
'''
Open() function have 2 params

file_name and mode of opening

modes are - r,a,w,x(creates)

print(f.read())

f.read(5) # read only first 5 chars

readline
readlines

close

To append :

f=open('filename.txt','a')
f.write('Hiii')
f.close()

to delete:

import os
os.remove('name')

if os.path.exists("demofile.txt"):

To remove folder :

os.rmdir("myfolder")


Numpy:
pip
np.array([])
2d array 
np.array([[],[]])

variable_name.ndim
Accessing elements of nparray 1d and 2d
a[1,5]
Slicing
Copy Function
view function
shape arr.shape
arr.reshare(r,c)
arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.array([[5, 6], [7, 8]])
np.concatenate((arr1,arr2),axis=1)
split:
np.array_split(arr,number_of_arrays)
Search:
np.where(arr == 4) #returns index
sort
Adding matrices of 2d arrays in np
np.add()

Pandas:
pip

df=pd.read_csv('')

Series- Like a column in table
a=[1,2,3]
pd.series(a)

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories)

print(myvar)

Dataframes-
df.loc[0] #returns first row
pd.read_csv()
df.head()
df.tail()

#Cleaning Data:

drop rows with empty cells:
df.dropna()
#replace empty values:
df.fillna(120,inplace=True)
df['column_name'].fillna(120,inplace=True)
df['column_name'].mean,median,mode

'''





