
import random
import time


labels = ['rock', 'paper', 'scissors']
num_rounds = 0
player_score = 0
computer_score = 0
countdown = 0
winner = []
computer_choice = random.choice(labels)
player_choice = []
class RPS:
    def __init__(self, player_choice, computer_choice, player_score, computer_score, winner, num_rounds):
        self.player_choice = player_choice
        self.computer_choice = computer_choice
        self.player_choice = player_choice
        self.computer_choice = computer_choice
        self.player_score = player_score
        self.computer_score = computer_score
        self.winner = winner
        self.num_rounds = num_rounds
      
        
    
            
    def play_game(self, player_choice, computer_choice):
        
        self.player_choice = player_choice
        self.computer_choice = computer_choice
        
        while True:
            if self.player_choice == 'rock':
                if self.computer_choice == 'paper':
                    print(self.computer_choice, '\nYou LOSE!')
                    self.computer_score += 1
                    self.num_rounds += 1
                    print(f'Computer score is: ', self.computer_score)
                    print(f'Number of rounds: ', self.num_rounds)
                    print('Your current score is: ', self.player_score)
                if self.computer_choice == 'scissors':
                    print(self.computer_choice, '\nYou WIN!')
                    self.player_score += 1
                    self.num_rounds += 1
                    print(f'Computer score is: ', self.computer_score)
                    print(f'Number of rounds: ', self.num_rounds)
                    print('Your current score is: ', self.player_score)
                elif self.player_choice == self.computer_choice:
                    print(self.computer_choice, '\nIts a TIE!')
            
            elif self.player_choice == 'paper':
                if self.computer_choice == 'rock':
                    print(self.computer_choice, '\nYou WIN!')
                    self.player_score += 1
                    self.num_rounds += 1
                    print(f'Computer score is: ', self.computer_score)
                    print(f'Number of rounds: ', self.num_rounds)
                    print('Your current score is: ', self.player_score)
                if self.computer_choice == 'scissors':
                    print(self.computer_choice, '\nYou LOSE!')
                    self.computer_score += 1
                    self.num_rounds += 1
                    print(f'Computer score is: ', self.computer_score)
                    print(f'Number of rounds: ', self.num_rounds)
                    print('Your current score is: ', self.player_score)
                elif self.player_choice == self.computer_choice:
                    print(self.computer_choice, '\nIts a TIE!')
            
            elif self.player_choice == 'scissors':
                if self.computer_choice == 'paper':
                    print(self.computer_choice, '\nYou WIN!')
                    self.player_score += 1
                    self.num_rounds += 1
                    print(f'Computer score is: ', self.computer_score)
                    print(f'Number of rounds: ', self.num_rounds)
                    print('Your current score is: ', player_score)
                if self.computer_choice == 'rock':
                    print(self.computer_choice, '\nYou Lose!')
                    self.computer_score += 1
                    self.num_rounds += 1
                    print(f'Computer score is: ', self.computer_score)
                    print(f'Number of rounds: ', self.num_rounds)
                    print('Your current score is: ', self.player_score)
                elif self.player_choice == self.computer_choice:
                    print(self.computer_choice, '\nIts a TIE!')
    def game_winner(self):                
        if player_score >= 3:
            self.winner = self.player_choice 
            countdown = 5
            for x in range(5):
                countdown -= 1
                print('Guessing...')
                time.sleep(5)
                print(f'Computer Picked: ',self.computer_choice)   
                print('You are the WINNER!!')  
                play_again = input("Play again? (y/n): ")
                self.num_rounds = 0
                player_score = 0
                self.computer_score = 0
                if play_again != "y":
                    print("See you again ! BYE!!")
                break                 
        if self.computer_score >= 3:
            self.winner = self.computer_choice    
            print('Guessing...')
            time.sleep(5)
            print(f'Computer Picked: ',self.computer_choice)
            print ('Computer is the WINNER!!')
            play_again = input("Play again? (y/n): ")
            self.num_rounds = 0
            self.player_score = 0
            self.computer_score = 0
            if play_again != "y":
                print("See you again ! BYE!!")
                
    def play_choice(self):
        while True:
            player_choice = input("Enter your choice (rock, paper, scissors): ").lower() 
            if player_choice != computer_choice:
                print('Please select from below list: \nrock, \npaper, \nscissors')  
              
                    
    def play_RPS(self):
        
        self.play_game()
        self.play_choice()    
            
                    
if __name__ == '__main__':            
    game = RPS(player_choice , computer_choice , player_score , computer_score , winner ,num_rounds)  
    game.play_game(player_choice, computer_choice)
                
