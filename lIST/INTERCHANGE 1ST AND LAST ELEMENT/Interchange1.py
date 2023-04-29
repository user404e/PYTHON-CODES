# INTERCHANGE 1ST AND LAST ELEMENT IN LIST

def Interchange(lst):
    temp = lst[-1]
    lst[-1] = lst[0]
    lst[0] = temp
    return lst

lst = [1,2,3,4,5]
print(Interchange(lst))
