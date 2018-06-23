def isPalindrome(word):
    word = word.lower()
    word = word.replace(' ', '')
    lenOfOriginalWord = len(word)
    if lenOfOriginalWord == 0:
        return False

    remainder = 1
    if lenOfOriginalWord % 2 == 0:
        remainder = 0
    while len(word) != remainder:
        firstCharacter = word[0]
        lastCharacter = word[len(word) - 1]
        if firstCharacter != lastCharacter:
            return False
        word = word[1 : len(word) -1]
    return True

def longestPalindrome(word):
    largestPalindrome = 0
    for i in range(0, len(word)):
        for j in range(i, len(word)):
            subStringOfWord = word[i:j+1]


            if isPalindrome(subStringOfWord):
                lenOfSubStringOfWord = len(subStringOfWord)

                if largestPalindrome < lenOfSubStringOfWord:
                    largestPalindrome = lenOfSubStringOfWord
                    palString = subStringOfWord
    print(palString)
    return largestPalindrome


print(longestPalindrome('aaathjmk'))
print(longestPalindrome('banana'))
print(longestPalindrome('asdfghgfdsa'))
print(longestPalindrome('alakajahagaf'))
