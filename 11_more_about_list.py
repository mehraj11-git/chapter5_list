# generate list with range function
# something more abput pop method
# index method
# pass list to a function 
num = list(range(1,11))
number = [1,2,3,4,5,6,7,8,9,10]
print(number,end="20")

print(number.pop(17))
print(number)
print(number.index(30))
print(number[::-1]) #use this code to print the data reverse

def negative_list(l):
    negative = []
    for i in l:
        negative.append(-i)
    return negative
    
print(negative_list(number))

# we can do range func in list 
# pop method return the deleted item
