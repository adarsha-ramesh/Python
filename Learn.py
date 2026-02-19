#Exercise 2: Manipulating a Python list.
import pandas as pd

a= [1,2,3,4,5]
a.append(6)                    #adds new number
a.remove(1)                    #removes second item from list
a.sort(reverse=True)           #prints none as the function is designed to only sort
print(a)                       #shallowcopy
print(sorted(a,reverse =True)) #permanent change

#Exercise 3: Conditional Logic
score = int(input("what is your score:"))
if score >= 40:
    print("You Passed")
elif score >= 80:
    print("You Failed")

#Team Lab Work:Title: The Data Automation Project
temperature_c = [22, 32, 43, 18, 0]

def fahrenheit(t):
    f= (t * 1.8) +32
    return f

for t in temperature_c:
    print(fahrenheit(t))

#Assignment 2: Function Builder: Write a Python script that contains at least three different functions.
a= 3
b=4
c= [1,2,3,4,5]
d="shivaya"
def add(a,b):
    print(a+b)
def highest(c):
    print(max(c))
def upper(d):
    print(d.upper())

add(a,b)
highest(c)
upper(d)


#Assignment 3: perform basic data manipulations and calculations
'''From a dictionary:
When you do pd.DataFrame(dataset_dict), pandas uses the dict keys as column names automatically. 
So you get nice labels like id, name, age, city, salary.
From a list of lists:
When you do pd.DataFrame(dataset_list) directly, pandas doesn’t know which row (if any) is the header. 
It treats every inner list as a data row and assigns default numeric column names (0, 1, 2, ...).'''

import pandas as pd

dataset_dict = {
    "id": [1, 2, 3],
    "name": ["Alice", "Bob", "Charlie"],
    "age": [25, 30, 22],
    "city": ["London", "Manchester", "Birmingham"],
    "salary": [48000, 52000, 45000]  # in GBP
}
dataset_list = [
    ["id", "name", "age", "city", "salary"],
    [1, "Alice", 25, "London", 48000],
    [2, "Bob", 30, "Manchester", 52000],
    [3, "Charlie", 22, "Birmingham", 45000]
]
name = dataset_dict["name"][dataset_dict["salary"].index(max(dataset_dict["salary"]))]
print(name)
name = max(dataset_list[1:], key=lambda x: x[4])[1]
print(name)

df=pd.DataFrame(dataset_dict)
print(df["salary"].mean())






