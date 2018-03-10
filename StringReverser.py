reverseStr = ""

strToReverse = input("Enter a word: ")
length = len(strToReverse)

for x in range(length - 1, -1, -1):
    print(x)
    reverseStr += (strToReverse[x])
print(reverseStr)
