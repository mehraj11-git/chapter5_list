# def a func that contain list and yoiu have to return two list one with even num and other with odd num




number = [1,2,3,4,5,5,6,7,8,0,10]
def integer_list(l):
    odd = []
    even = []
    for i in l:
      if i % 2 == 0:
        even.append(i)
      else:
        odd.append(i)    
    output = [odd,even]
    return output
print(integer_list(number))        
