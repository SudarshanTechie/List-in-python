"""
List:
-list are the collection of ordered and mutable data
-multiple datatypes can be written inside list

Syntax
l=["apple",",mango",1,34.89]
"""
l=["Ironman","Thor","Captain America","Hulk"]
print(l)
print(type(l))
print(l[1]) #print the element at index 1
print(l[3]) #print the element at index 3

# slicing of list
print(l[1:3]) #print from one to three
print(l[:2]) #starts with zero and end at 2
print(l[1:]) #stars with 1 to end
print(l[::2]) # gap of two
print(l[-3:-1]) #negative indexing

# list iteration
# using loop
l2=[10,20,30,40,50,60]
for i in l2:
    print(i)
# using length function
for i in range(0,len(l2)):
    print(l2[i])
# using while loop
i=0
while i<len(l2):
    print(l2[i])
    i=i+1
