def ispalindrome(s):
    lst = []
    lst.extend(s)
    lst2 = lst
    lst.reverse()
    if lst == lst2:
        return True
    else:
        return False

s = input("Enter String To Check It Is Palindrome Or Not : ")
print(ispalindrome(s))
