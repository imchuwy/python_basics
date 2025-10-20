'''
2h 48m
If you don't put a RETURN statement. Python will return None
'''

def square(number):
    return number*number
#print(square(3))

#Task one. Make the below into a function
#message1 = input('>')
#sentence1 = message1.split(' ')
#output1 = ' '
#emojis1 = {
#    ':)': '😊',
#    ':(': '😒'
#}
#output1 = ''
#for word1 in sentence1:
#    output1 += emojis1.get(word1, word1) + ' '


#My attempt
def lookup(message):
    sentence = message.split(' ')
    emojis = {
        ':)': '😊',
        ':(': '😒'
    }
    output = ''
    for word in sentence:
        output += emojis.get(word, word) + ' '
    return output

#Dont forget two blank lines between function


message = input('>')
print(lookup(message))