'''
[] Square brackets show list
We can use indexes on list

'''
names = ['oscar','alicia','bob','dylan']
#print(names[1:3])

names[2] = 'bobby'
#print(names)


#Find largest number in list
list = [5,1,3,7,2,9,99,5]
x = 0
for i in list:
    if i > x:
        x = i
#print(x)

#List of methods
#list.append(20) #adds 20 to end
#list.insert(2, 10) #At position 2, insert 10
#list.remove(5) #removes first 5
#5 in list #boolean of where
#list.clear() #empties list
#list.pop() #removes last item
#list.sort() #sorts
#list.reverse() #sorts desc

x = list.index(5) #finds where 5 is
y = list.count(5) #counts the number of occurance
z = sorted(list, reverse=True)
list2 = list.copy() #copies

#print(z)


#List in list. To retrieve the list within the list. Use [][]
'''
matrix = [
    [1,2,3],
    [4,5,9],
    [7,8,9]
]
print(matrix[0][1])

for row in matrix:
    for cell in row:
        print(cell)
'''


#Task. Remove duplicates in list
dupe_list = [5,5,5,1,23,23,23,5,7,23,9,99,25,99,23]

#My method. Remove existing duplicates. This does not work because Python skips over the next item in the list when we remove it
for i in dupe_list:
    x = dupe_list.count(i)
    if x > 1:
        dupe_list.remove(i)

#Instead. Create new list
dupe_list1 = dupe_list
for i in dupe_list1[:]:  # loop over a COPY to avoid skipping elements
    if dupe_list1.count(i) > 1:
        dupe_list1.remove(i)  # removes only 1 duplicate at a time

#Shown method. Copy non-duplicates into new list
dupe_list2 = dupe_list
uniques = []
for i in dupe_list2:
    if i not in uniques:
        uniques.append(i)

print(dupe_list2)