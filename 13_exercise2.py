# def a func which will take list as as argument and this func will return a reverse list

# simple reverse method
# in this we use reverse method
number=[1,2,3,4]
def reverse_list(l):
   l.reverse()
   return l
print(reverse_list(number))

# string reverse method
yoyo=[1,2,3,4]
def list(l):
   return l [::-1]
print(list(yoyo))  

# using pop and append method
number = [1,2,3,4]
def reverse_list(l):
    reverse = []
    for i in range(len(l)):
      popped_item = l.pop()
      reverse.append(popped_item)
    return reverse
print(reverse_list(number))  

