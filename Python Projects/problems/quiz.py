from time import *
import threading



name = input("Enter your name: ")

def countdown():
    global my_timer

    my_timer = 30
    
    for i in range(my_timer):
        my_timer = my_timer - 1
        sleep(1)
    
    print("**** Time's Up ****")

countdown_thread = threading.Thread(target = countdown)

countdown_thread.start()


def gkquiz(name):
    global score

    score  = 0
    while my_timer > 0:

        print("GK Quiz")

        print("Question 1: ")
        sleep(1.0) 
        print("What is the capital of India?")
        sleep(1.0)
        print("A.       Mumbai")
        sleep(0.5)
        print("B.       Shimla")
        sleep(0.5)
        print("C.       New Delhi")
        sleep(0.5)
        print("D.       Manali")
        sleep(0.5)
        Answer = input("Please enter your answer: ")
        if Answer == "c":
            print("Correct")
            score = score + 10
            print(f"{name}, Your score is, {score}")
        else:
            print("incorrect")
            print(f"Your score is, {score}")
        
        sleep(2.0)

        if my_timer == 0:
            break


        print(" Question 2: ")
        sleep(1.0) 
        print("What is the full for of www?")
        sleep(1.0)
        print("A.       world wide web")
        sleep(0.5)
        print("B.       world west wide")
        sleep(0.5)
        print("C.       world work west")
        sleep(0.5)
        print("D.       word wide world")
        sleep(0.5)
        Answer = input("Please enter your answer: ")
        if Answer == "a":
            print("Correct")
            score = score + 10
            print(f"{name}, Your score is, {score}")
        else:
            print("incorrect")
            print(f"Your score is, {score}")
        
        sleep(1)

        if my_timer == 0:
            break


        print("Question 3: ")
        sleep(1.0) 
        print("Which one is the Python web framwork?")
        sleep(1.0)
        print("A.       Vue")
        sleep(0.5)
        print("B.       Bulma")
        sleep(0.5)
        print("C.       Django")
        sleep(0.5)
        print("D.       API")
        sleep(0.5)
        Answer = input("Please enter your answer: ")
        if Answer == "c":
            print("Correct")
            score = score + 10
            print(f"{name}, Your score is, {score}")
        else:
            print("incorrect")
            print(f"Your score is, {score}")
        
        sleep(1)

        if my_timer == 0:
            break

        print("Question 4: ")
        sleep(1.0) 
        print("Who is the founder of Tesla?")
        sleep(1.0)
        print("A.       Jhon Cena")
        sleep(0.5)
        print("B.       Elon musk")
        sleep(0.5)
        print("C.       You")
        sleep(0.5)
        print("D.       Steve jobs")
        sleep(0.5)
        Answer = input("Please enter your answer: ")
        if Answer == "b":
            print("Correct")
            score = score + 10
            print(f"{name}, Your score is, {score}")
        else:
            print("incorrect")
            print(f"Your score is, {score}")
        
        sleep(1)

        if my_timer == 0:
            break


        print("Question 5: ")
        sleep(1.0) 
        print("How many Seconds are in a mintue")
        sleep(1.0)
        print("A.       50")
        sleep(0.5)
        print("B.       60")
        sleep(0.5)
        print("C.       70")
        sleep(0.5)
        print("D.       81")
        sleep(0.5)
        Answer = input("Please enter your answer: ")
        if Answer == "b":
            print("Correct")
            score = score + 10
            print(f"{name}, Your score is, {score}")
        else:
            print("incorrect")
            print(f"Your score is, {score}")
        
        sleep(1)
        if my_timer == 0:
            break
    
    return score
    
    


gk = gkquiz(name)
print("********")
print(f"{name} your final score is, {score}")


    