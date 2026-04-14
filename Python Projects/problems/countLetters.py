
def countLetter(word, letter):
    counter = 0
    for i in range(0, len(word)):
        for j in range(0, len(word[i])):
            if letter == word[i][j]:
                counter += 1
    return counter 


word = input("enter the words with space:- ")
letter = input("Enter the letter you want to count:-  ")

c = countLetter(word, letter)

print(f"There are {c} {letter} in the list")