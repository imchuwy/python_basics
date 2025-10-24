
# For loop that will start at 1, end at 20, and choose every 2
x = []
for number in range(1, 20, 2):
    x.append(f"attempt {number + 1} {(number + 1) * '.'}")
# print("\n".join(x))


# Breaking loops
Test = "Bye"
for number in range(5):
    if Test == "Hello":
        y = "Successful"
        break
else:
    y = "Attempted and failed"
# print(y)


# Nested loops
for x in range(3):
    for y in range(2):
        for z in range(1):
            # print(f"({x}, {y}, {z})")
            break

        # Some complex objects are iterable. (String, range, list)
range = type(range(5))
string = "Python"
list = [1, 2, 4, 3]

for x in list:
    print(x * 0.5)


# Exercise to print ever even number between range(1, X). Then show how many even numbers count there are.
count = 0
for i in range(1, 200):
    if i % 2 == 0:
        count += 1
        print(i)
print(f"We have {count} even numbers")
