"""
list comprehension
-to copy data from one list to another list
-we can apply some conditions on it to copy data

"""
l1=[10,20,30,40,50,60]
l2=[]
l3=[]
# simply copy data from one list to another
for i in l1:
    l2.append(i)
print(l2)

#we can apply condition to copy data
for i in l1:
    if i>45:
        l3.append(i)
print(l3)

# instead of doing all above stuff we can do this in one line
l4=[i for i in l1] #this is list comprehension without condition
l5=[i for i in l1 if i>45] #list comprehension with condition
print(l4)
print(l5)