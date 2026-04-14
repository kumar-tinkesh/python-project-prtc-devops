def countLetter(word, letter):
    counter = 0
    for i in range(0, len(word)):
        for j in range(0, len(word[i])):
            if letter == word[i][j]:
                print(i, j, letter)
                counter += 1

    return counter 



word= input("Enter your word:  ")
letter = input("Enter the letter you want to count:  ")
print(countLetter(word, letter ))