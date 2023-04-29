# INTERCHANGE 1ST ANF LAST ELEMENT IN LIST

lst = [1,2,3,4,5]

temp = lst[-1]
lst[-1] = lst[0]
lst[0] = temp

print(lst)
