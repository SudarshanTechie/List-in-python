#functions of list

l=[12,56,79,78,53,90,64,12]
#len() returns the length of list
print(len(l))

# count() to find occurence of perticular element
print(l.count(56))
print(l.count(12))

# append() to add element to the list at end
l.append(232)
print(l) #232 will be add at the end

# insert() to add element at specific location
l.insert(2,59)
print(l) #59 will be add at index 2

# remove() to remove specific element from list
l.remove(90)
print(l) #90 will from list

# pop() to remove element from certain location
print(l.pop(6)) #removes element at index 6

# copy() to create a copy of list
l2=l.copy()
print(l2)

# index() to access index of certain element
print(l.index(56))

# extend() to add two lists
b=[10,20]
l.extend(b)
print(l)

# reverse() to reverse the list
l.reverse()
print(l)

# sort() to sort the list
l.sort()
print(l)

# clear() to remove all elements from the list
l.clear()
print(l)