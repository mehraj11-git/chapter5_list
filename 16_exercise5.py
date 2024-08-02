# number1 = [1,2,4,5,],[1,2,7,8]
# def a func and take two list and return the common number 
def common_element(l1, l2):
    output = []
    for i in l1:
        if i in l2:
            output.append(i)
    return output
print(common_element([1,2,4,5,],[1,2,7,8]))        
