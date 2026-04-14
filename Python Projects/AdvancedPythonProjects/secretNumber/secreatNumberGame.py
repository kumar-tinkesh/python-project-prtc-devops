import random 

number_of_digits = 3
max_guseses = 10

def main():
    print("Guess The Secreat Number")
    print(f"You will see a {number_of_digits} digits number with no repeated digit.\n Try guessing it..")
    print("Few hints for you: ")
    print("""
        If message is X. Your one digit is correct but on the wrong place.\n
        if message is Y. One digit is correct. and on the right place.
        If message is Z. No digit is correct.\n

        if the secret number is 789 and your guess is 985, message would be\n
        YX
    """)

    while True:
        secretNumber = getSecrtNumber()
        print("Guess the number: ")
        print("You have {max_gusess}")

        numGuseses = 1
        while numGuseses <= max_guseses:
            guess = ""
            while len(guess) != number_of_digits or not guess.isdecimal():
                print(f"Guess -{numGuseses}")


def getSecrtNumber():
    numbers = list('0123456789')
    random.shuffle(numbers)
    secrtNum= ""
    for i in range(number_of_digits):
        secrtNum += str(numbers[i])
    return secrtNum



def getClues(guess, secretNumber)            :
    if guess == secretNumber:
        return "You got the correct answer"
    
    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNumber[i]:
            clues.append('Y')
        elif guess[i] in secretNumber:
            clues.append('X')

    if len(clues) ==0:
        return 'Z'
    else:
        clues.sort()
        return "".join(clues)
    
    


