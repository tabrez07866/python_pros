# list=[]

# list.append(5)
# list.append(5)
# list.append(5)
# list.append(6)
# list.append(7)

# print(list)
# print("element at index 1: ",list[1])
# print("Count of 5: ",list.count(5))
# print("Index of element 7 : ",list.index(7))
# list.insert(0,10) #insert 10 at index 0
# print("Length of list or Array",len(list)) #length of list

# list.extend([1,2,4])

# newList=list.copy()
# print("New Copy list",newList)

# print("Popped ele",list.pop())

# list.reverse()

# list.sort()

# print(list)

# list.clear()
# print(list)


#######################################################################



# set=set()

# set.add(1)
# set.add(2)
# set.add(3)
# set.add(4)
# set.add(4)
# set.add(5)
# set.add(6)
# set.add(7)

# print("length of set: ",len(set))
# set.pop()
# set.pop()
# set.pop()

# print("set after pop",set)

# set.difference()

# newSet=set.copy()
# print("New copy set: ",newSet)
# print(set)



# set.clear()
# print("clear set = ",set)

set1={4,5,6,7}
set2={4,5,6,7,8}

# print(set1.difference(set2))
# print(set1.difference_update(set2))
# print(set1.discard(set2))
# print(set1.intersection(set2))
# print(set1.isdisjoint(set2))
# print(set1.issubset(set2))
# print(set1.issuperset(set2))
# print(set1.symmetric_difference(set2))

record={
    "roll":1,
    "name":"tabrez",
    "dept":"cse"
}

print(record)
print(record.get('name'))
for key,va in record.items():
    print(f"{key}-{va}")

students=[]


students.append(record)
print(students)

students.append({
    "roll":2,
    "name":"xisham",
    "dept":"ee"
})


students.append({
    "roll":3,
    "name":"zisham",
    "dept":"me"
})

print(students)

print(students[0])
print(students[1])
print(students[2])

for i in range(len(students)):
    for key,value in students[i].items():
        print(f"{key}-{value}")


for i in range(3):
    print(i)
