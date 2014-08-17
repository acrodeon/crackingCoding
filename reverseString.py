#################################################################################################
# Write code to reverse a C-Style String.                                                       #
# (C-String means that “abcd” is represented as five characters, including the null character.) #
#################################################################################################


word  = "carlos is amazing"
print(word)

wordList = list(word)

start = 0
end = len(wordList) - 1

# or wordList.reverse()
while start < end :
    wordList[start], wordList[end] = wordList[end], wordList[start]
    start += 1
    end -= 1

for i in wordList:
    print(i, sep = '', end = '')
print()


