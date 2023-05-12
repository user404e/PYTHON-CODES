num = int(input("Enter Number : "))

flag = True

for i in range(2,num):
    if(num%i==0):
        flag = False
        break

if(flag):
    print("PRIME")
else:
    print("NOT PRIME")