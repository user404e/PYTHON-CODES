lst = [32,5,23,53,323,5,46,35,534,532,4]

print("List Items :-\n")
for i in lst:
    print(i,end=" ")

lst.sort()

n = int(input("\n\nEnter N : "))

nth_largest_number = lst[n-1]

print(n , "SMALLEST NUMBER =" , nth_largest_number)