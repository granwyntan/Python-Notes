word = input("Enter a word to check if its a palindrome: ")
word = word.lower()
word = word.replace(" ", "")
print(word)
isPalindrome = False
if word[::-1] == word:
    isPalindrome = True

if isPalindrome:
    print("Word is a Palindrome")
else:
    print("Word is not Palindrome")
