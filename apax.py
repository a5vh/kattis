word = list(input())
for i in range(len(word)):
    if i + 1 <= len(word)-1:
        if word[i] == word[i+1]:
            wow = 1
            print(word)
            while word[i] == word[i+wow]:
                wow += 1
            for he in range(wow):
                word.remove(word[i+he])
                print(word)

print(word)
