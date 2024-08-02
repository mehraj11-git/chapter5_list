# count
# sorted function
# reverse
# clear
# copy

# count method
# if you want to count the data we uae this method
# sort method 
# use this method to arrange data in alphabetical order 
# sorted func
# this method donot sort the main list but it sorted the items in list 
# clear method:
# this method clear the list
# copy method 
# use to copy list
# yoyo.clear()
# yoyo.copy() 
yoyo=["apple","mango","banana","grapes,kiwi"]
print(yoyo.count("banana"))
print(yoyo)
yoyo1=["apple","mango","banana","grapes","kiwi","apple"]
print(yoyo1.count("apple"))
 

 #sorted func
string=["apple","mango","banana","grapes,kiwi"]
number=[3,1,54,67,2,4,3,]
string.sort()
number.sort()
print(number)
print(string)
print(sorted(string))
number.clear()
print(number)
number_copy = number.copy()
print(number_copy)