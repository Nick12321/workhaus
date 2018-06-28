def checkPalindrome(word):
    word = word.lower()
    word = word.replace(' ', '')
    lenOfOriginalWord = len(word)
    if lenOfOriginalWord == 0:
        return "Not Palindrome"

    remainder = 1
    if lenOfOriginalWord % 2 == 0:
        remainder = 0
    while len(word) != remainder:
        firstCharacter = word[0]
        lastCharacter = [len(word) - 1]
        if firstCharacter != lastCharacter:
            return "Not a Palindrome"
        word = word[1 : len(word) - 1]
    return "Palindrome"

print(checkPalindrome('Anna'))
print(checkPalindrome('bob'))
print(checkPalindrome('boxb'))
print(checkPalindrome(' '))
