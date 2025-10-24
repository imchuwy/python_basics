

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