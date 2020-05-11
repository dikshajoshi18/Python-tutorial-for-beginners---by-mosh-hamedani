#programming with mosh
print("diksha")
print ('0----')
print("||||")
print('&' * 10)
#variables
price=10
print(price)
rating=8.9
name="diksha"
is_published= False#WITH CAPITAL F
#EXERCISE
name='john smith'
age1=20
new_patient= True
#getting inputt
name= input('what is your name?')
print('hi ' + name) #concatenation
#exercise
personname=input('what is your name ?')
fav_color=input('what is your fav color?')
print(personname + " likes " + fav_color)
#type conversion
birth_year=input('birth year:')
age = 2020-int(birth_year)
print(age)
print(type(birth_year))
print(type(age))
#exercise
weight=float(input("whats your weightt in pounds"))
kg_wt= 0.45*weight
print(kg_wt) 
#strings
#adding apostrophe
course="python's course for beginners"
#adding double quotes
course1='python course for "begginers"'
#multiline string
email=''''''hi  dear
this is our first email to you
thank you
contact:686486288
'''
'''print(course)
print(course1)
print(email)
#indexing
course='python'
print(course[0])
print(course[-1])
#slicing
sliced='python'
print(sliced[0:])
print(sliced[0:3])
print(sliced[1:4])
print(sliced[:4])
print(sliced[:])
name="jenifer"
print(name[1:-1])
#formatted strings
first="john"
last="smith"
message=first + '['+last+'] is a coder' 
#msg=f '{first} [{last}] is a coder'
print(message)
#string methods
text="python for all"
print(len(text))
print(text.upper())
print(text.lower())
#reverse indexing
print(text.find('p'))
#sequence of char
print(text.find('all'))
print(text.replace('all','beginners'))
#boolean in string
print('python' in text)
#arithmetic operations
print(10+3)
print(10/3)
print(10//3)
print(10%3)
print(10**3)
print(10-3)
print(10*3)
x=10
x=x+3
print(x)
#augmented assignment operator
x+=3
x-=3
print (x)
#operator precedence
x=10+3*2
print(x)
#using paranthesis to change the order
x=(10+3)*(5-2)
print(x)
#math functions
x=5.6
print(round(x))
print(abs(-4.5))
import math
print(math.ceil(2.9))
print(math.floor(2.9))
#conditional statements
is_hot=True
is_cold= False
if is_hot:
    print("it's a hot day")
elif is_cold:
    print("its a cold day")
else:
    print("its a lovely day")
#exercise
price=1000000
good_credit=True
if good_credit:
    down_pay=0.1*price
    print(float(down_pay))
else:
    down_pay=0.2*price
    print(float(down_pay))
#logical operators
high_income= True
has_good_credit= False
criminal_rec= True
if has_good_credit and high_income:
    print("eligible")
if has_good_credit and not criminal_rec:
    print("elgible")
#conditional
temp= 33
if ((temp)>=30) :
    print ("its a hot dayy")
elif (temp<10):
    print("its cold day")
else:
    print("neither hot nor cold")
#exercise
name="diksha"
if (len(name)<3):
    print("name must be 3 char long")
elif (len(name)>50):
    print("name can be of max 50 char")
else :
    print("name looks good")
#project
weight=int(input("enter your weight"))
unit=input("l is for lbs k is for kg")
if(unit.upper() =="L"):
    convertedvalue= weight*0.45
    print(f"you are {convertedvalue} kilos")
else:
    convertedvalue=weight/0.45
    print(f"you are {convertedvalue} pounds")
#loops in python 
# while loop
i=1
while (i<=5):
    print(i*'&')
    i= i+1
print("done")
#guessing game
secret_number=8
gduess_count=0
guess_limit=3
while(guess_count<guess_limit):
    guess=int(input(("guess:")))
    guess_count+=1
    if(guess==secret_number):
        print("you won")
        break
else:
    print("sorry! you lose")
#exercise
command= input("> ").lower()
started= False
while (True):
    
    if(command=="start"):
         if started:
            print("car is already started there is no point in starting it twice")
         else :
            started=True
            print ("car started")

    elif(command=="stop"):
        if not started:
            print("car is already stoppedd there is no point in stopping it twice")
        else:
            started= False
            print("car stopped")
    elif(command=="help"):
         print(
'''start-to start the car
stop-to stop the car
quit- to quit''')
    elif(command=="quit"):
        print("quit from here")
        break
    else:
       # print("i dont understand that")
#for loops
for item in "python":
    print(item)
for item in range(0,10):
    print(item)
for i in range (2,10,2):
    print(i)
prices=[10,38,276,8,7,8,9]
total=0
for i in prices:
    total+=i
    print(total)
#generating list of coordinatte
for x in range(4):
    for y in range(4,8):
        print(f"({x},{y})")
#exercise to print F
numbers=[5,2,5,2,2]
for i in numbers:
    print(i*"*")
# to print L
numbers2=[1,1,1,1,5]
for i in numbers2:
    print(i*'x')
#lists
#2 D list
#matrix
matrix=[[1,2,3],
[4,5,6],
[7,8,9]]
#matrix indexing
print(matrix[0] [1])
for row in matrix:
    for item in row:
        print(item)
#list methods
numbers.append(23)
print(numbers)
numbers.insert(0,10)
numbers.remove(2)
numbers.pop()
numbers.index(5)
print(50 in numbers)
numbers.count(5)
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
num=numbers.copy()
numbers.append(10)
print(num)
#exercise
list1=[2,4,2,1,4,6,1,4,6,3,2]
list2=[]
for i in list1:
    if i not in list2:
        list2.append(i)
print(list2)
#tuples
#ccant be modified or immutable
numb=(1,2,3,4)
print(numb.count(2))
print(numb.index(2))
#unpacking
coordinates=(1,2,5)
x=coordinates[0]
y=coordinates[1]
z=coordinates[2]
x,y,z=coordinates
print(x,y,z)
#dictionaries
customer={
    "name":"diksha",
    "age": 19,
    "verified": True
}
print(customer["name"])
print(customer.get("name"))
print(customer.get("birthdate","1 jan"))
#exercise
phone=(input("enter the phone number"))
digit_mapping={
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four",
    "5":"five",
    "6":"six",
    "7":"seven",
    "8":"eight",
    "9":"nine",
    "0":"zero"
}
output=""
for i in phone:
    output += digit_mapping.get(i,"!")+(" ")
print(output)

#emogi converter
message=input("enter a message>")
words=message.split("")
print(words)
emojis={
    ";)": "😉",
    ":)": "😊",

    ":*" : "😘"

}
output=""
for word in words:
    output+=emojis.get(word,word)
print(output)   


#functions
def greet_user():
    print("hi there")
    print("welcome aboard")


print("start")
greet_user()
print("finish")
#using parameters
def greet_user(name):
    print("hi there",name)
    print("welcome aboard")


print("start")
greet_user("diksha");
print("finish")
#using arguments
def greet_user(first_name,last_name):
    print(f"hi {first_name}{last_name}!")
    print("welcome aboard")


print("start")
greet_user("diksha","joshi");
print("finish")
#square of a number
def square(number):
    return(number*number)


#result=square(8)
#print(result)
print(square(9)) 
#emogi converter with functions
def emoji_con(msg):
    wrds=msg.split (" ")
    emoji={
        ";)": "😉",
        ":)": "😊",
        ":*" : "😘"
    }
 
    output=""
    for i in wrds: 
        output += emoji_con.get(i,i)+" "
    return output
msg=input("enter the message")
print(emoji_con(msg))

#exceptinal handling
try:
    age= int(input("age"))
    print (age)
except ValueError:
    print("invalid value")
#other one
try:
    age=int (input("age:"))
    income=20000
    risk=income/age
    print(age)
except ZeroDivisionError:
    print("age cannot be zero")
except ValueError:
    print("invalid value")
 
 #comments
 #print ("skyy is blueee")
#classes
class Point :
    def move(self):
        print("move")

    def draw(self):
        print("draw")


point1=Point()
point1.x=10
point1.y=20
print(point1.x)
point1.draw()

point2= Point()
point2.x=1
print(point2.x) 
#constructors
class Point:
    def __init__(self,x,y):#initialise an objectt as constructtor
        self.x=x
        self.y=y
    def move(self):
        print("move")

    def draw(self):
        print("draw")


point=Point(10,20)
print(point.x)
#exercise
class Person:
    def __init__(self,name):
        self.name=name
    def talk(self):
        print(f"hi, I am {self.name}")

per=Person("diksha")
print(per.name)
per.talk()
#inheritence
class mammal:
    def walk (self):
        print("walk")


class dog(mammal):
    def bark(self):
        print("bark")


class cat(mammal):
    pass


dog1=dog()
dog1.bark()
#importing modules
#importing complete module
import converters

print(converters.kg_to_lbs(70))
#importing one function
from converters import kg_to_lbs

print(kg_to_lbs(70))

#exercise
import utils

numbers=[2,4,5,78,9]
maximum=utils.find_max(numbers)
print(maximum(numbers))

#importing packages
import ecommerce.shipping
ecommerce.shipping.calc_shipping()
#using from
from ecommerce.shipping import calc_shipping
calc_shipping()
#imporing complete module
from ecommerce import shipping
calc_shipping()
#generating random values
import random
for i in range (3):
    print(random.random())
    print(random.randint(10,20))
members=['john','mary','mosh']
leader=random.choice(members)
print(leader)
#exercise
#my method 
import random
for i in range (1):
    for j in range (1):
        roll1=random.randint(1,6)
        roll2=random.randint(1,6)
        print(f"({roll1} , {roll2})")
#mosh's method
import random


class dice:
    def roll(self):
        first=random.randint(1.6)
        second=random.randint(1,6)
        return first,second


dice=dice()
print(dice.roll())
#directories
from pathlib import Path
#absolute path
#relative path


path =Path("ecommerce")
print(path.exists())

path= Path("email")
print(path.mkdir())
print(path.rmdir())
from pathlib import Path
path= Path()
#search all py file in current directory
for file in path.glob("*.py"):
    print (file)

#pypi and pip (python package index )











