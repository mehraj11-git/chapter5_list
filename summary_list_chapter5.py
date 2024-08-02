# list = its a data structure that can hold any type of Data  
# list is created by using square bracket
# ex : words = ['word1','words2'] 
#  we can store anything in list (string and numbers) 
mixed = [1,2,3,4,'five',['sharat'],'seven',8,9] 
#  how to data in list 
# (1) append method : this methdod add a num or str at last item
# mixed.append('10')
# print(mixed)
# mixed.append([10,20,30])
# print(mixed)
# (2)extend method
#  it will add numbers or str as a separete data  
# ex:
# mixed.extend([10,20,30])
# print(mixed)
# (3) insert method
# by this method we can add anything where we want t0 add 
# ex:
# mixed.insert(1,'sharat')
# print(mixed) 
# how to delete data from list :
# (1) pop method this mwthod will delete data from last
# ex:
# mixed.pop()
# print(mixed)
# (2) remove method this method delete particular data from list
# ex:
# mixed.remove('seven')
# print(mixed) 
#(3) del statement : this method use index to delete particular data
# ex:
# del mixed[5]
# print(mixed)
# loop in list 
# for loop in list 
# ex:
# for i in mixed :
#     print(i)
#     if u want data side by side use this 
# for i in mixed :
#     print(i,end= " ")