#  def a func that take list of words as argument and return a list with reverse of every element in that list



words = ['abc','tuv','xyz']
def reverse_list(l):
    reverse = []
    for i in l:
        reverse.append(i[::-1])
    return reverse
print(reverse_list(words))