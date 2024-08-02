number = [[1,2,3],[4,5,6],[9,10],[2,53,5,24,]]
def type_list(l):
    output = 0
    for i in l:
        if type(i) == list:
         output +=1 
    return output        
print(type_list(number))        

#  def a func and contain list and return how many list we have
# it will show do we have list inside list 