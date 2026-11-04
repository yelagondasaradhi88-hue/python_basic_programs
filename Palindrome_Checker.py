s = input("Enter a word: ").lower()

if s==s[::-1]:
    print("it is a palindrome")
else:
    print("it is not a palindrome")