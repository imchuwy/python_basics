
# define some strings
first = "\"Oscar\""
last = "Chu's"

# function for concat. This is a formatted string
fullname = f"{first} {last}"

# function for showing string length
length = len(fullname)

# Method for all upper case
fullname_upper = fullname.upper()

# Other methods. Upper, Lower, Title, RStrip, Find, Replace
find = fullname.find("car")

# operators/expression. Returns boolean.
in_method = "poo" not in fullname

print(in_method)


'''
One useful method is split. This essentially is a delimiter
'''

message = 'I want donuts in ma belly'
splitlist = message.split(' ')
print(splitlist)
