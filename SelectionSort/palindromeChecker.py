
def checkForPalindrome(word):
    if len(word) < 2:
        return True
    elif word[0] == word[-1]:
        word = word[1:-1]
        return checkForPalindrome(word)
    else:
        return False

some_string = ""
print checkForPalindrome(some_string)