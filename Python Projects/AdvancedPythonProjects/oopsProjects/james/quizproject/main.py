from typing import List 

class Question:
    def __init__(self, prompt:str, answer:str):
        self.prompt = prompt
        self.answer = answer 


class Player:
    def __init__(self, name:str):
        self.name=name 
        self.score = 0




class Quiz:
    def __init__(self, questions:List[Question]):
        self.questions = questions
        self.players =[]

    def add_players(self, player:Player):
        """add a player to the game"""
        
        self.players.append(player)        

    def ask_questions(self):
       
        # get player from palyers
        for player in self.players:
            print(f"For {player.name} : ")
            # get question from questions
            for q in self.questions:
                answer = input(q.prompt)
                if answer.lower() == q.answer.lower():
                    player.score += 1   
                    print("CORRECT")
                    print("")
                else:
                    print("INCORRECT!")
                    print("")
            print(f"Player : {player.name}, score : {player.score}")


    def show_winner(self):
        """ show winner by comparing score"""
        
        winner = max(self.players, key=lambda p: p.score)
        print("")
        print(f"{winner.name} is the winner. Score {winner.score}")




questions = [
    Question("Capital of India: ", "Delhi"),
    Question("2 * 2: ", "4"),
    Question("is this vs code: ", 'yes')
]



player1 = Player("Alex")
player2 = Player("Tom")


quiz = Quiz(questions)
quiz.add_players(player1)
quiz.add_players(player2)
quiz.ask_questions()

quiz.show_winner()