def ispalindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False

s = input("Enter String To Check It Is Palindrome Or Not : ")
print(ispalindrome(s))
