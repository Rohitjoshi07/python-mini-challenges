# --------------
#Code starts here
def palindrome(num):
    new =num + 1
    while new>0:

        if str(new) == str(new)[::-1]:
            return new
        else:
            new += 1
            continue
   



# --------------
#Code starts here

def a_scramble(str_1,str_2):
    str_1 = str_1.lower()
    str_2 = str_2.lower()
    s1 = [i for i in str_1]
    s2 = [i for i in str_2]
    np = []   
    for i in s2:
        A= i in s1
        if A == True:
            np.append(i)
            s1.remove(i)
        else:
            continue
    if np == s2 :
        return True
    else:
        return False





# --------------
#Code starts here
import math 
def check_fib(num):
    a = (5*num**2) + 4
    b = (5*num**2) - 4
    a_root = math.sqrt(a)
    b_root = math.sqrt(b)
    if int(a_root + 0.5)**2 == a or int(b_root + 0.5)**2 == b:
       return True
    else:
        return False




# --------------
#Code starts here
from itertools import groupby
def compress(word):
    word = word.lower()
    groups = groupby(word)
    result =  [ (label,sum(1 for _ in group )) for label,group in groups ]
    final = "".join("{}{}".format(label, count) for label, count in result)
    return final


    


# --------------
#Code starts here
def k_distinct(string,k):
    string = string.lower()
    word = set([i for i in string])
    if len(word) == k:
        return True
    else:
        return False


