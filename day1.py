a=2
b=4
c=3 
d=4

print("hello missi")

print(35>25<20)

print(15**3)

v="hello"
s=None
w=5
print(type(v))
print(type(s))
print(type(w))

"""this is for comment"""
#this is also for comment

#Casting in variable
c=int (5)
b=str(5)
z=float(5)
print(c,b,z )

#assign multiple values
p,q,r = 23,"gommu",34.5
print(p,q,r)

#one value for multiple variables
a=s=d="gommu"
print(a +s +d)

#unpack a collection
fruits=["mango","gommu",3]
q=w=e=fruits
print(fruits)

#GLOBAL VARIABLES
x="OSM"
def myfunc():
    x="fantastic"
    print("Python is",x)
myfunc()
print(x)

#THE GLOBAL KEYWORD
x="OSM"
def myfunc():
    global x
    x="fantastic"
    print("Python is",x)
myfunc()
print("python is",x)

