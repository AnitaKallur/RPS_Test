import math
import cv2
from keras.models import load_model
import numpy as np
print('x' in np.arange(5))   #returns False, without Warning
import random
import time
model = load_model('keras_model.h5', compile = False)
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
labels = ['rock', 'paper', 'scissors']
num_rounds = 0
winner = []
timer = time.time()
player_score = 0
computer_score = 0
computer = random.choice(labels)
RPS = True

while RPS:
    # Indicates to get ready to play the game by keeping countdown.
    def countdown():
        print("Get, Set, Ready....")
        time.sleep(2)
        for x in range(3, 0, -1):
            print('Ready in {} seconds'.format(x))
        time.sleep(2)
        print('Play!')

    def user_input():
        global timer  
        model = load_model('keras_model.h5', compile = False)
        cap = cv2.VideoCapture(0)
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)     
        for i in range(0, 1):  
            ret, frame = cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            data[0] = normalized_image
            prediction = model.predict(data)
            cv2.imshow('frame', frame)
            # get camera hand gestures translated into intended class          
            model_labels = ['rock', 'paper', 'scissors', 'nothing']
            get_max = max(range(len(prediction)))
            human_prediction = model_labels[get_max]

            if prediction[0][0] > 0.5:
                human_prediction = 'rock'
            elif prediction[0][1] > 0.5:
                human_prediction = 'paper'
            elif prediction[0][2] > 0.5:
                human_prediction = 'scissors'
            else:
                human_prediction = 'nothing'
                
        # After the loop release the cap object
        cap.release()
        # Destroy all the windows
        cv2.destroyAllWindows()
        print ('\nPlayer choice is: ', human_prediction)
        global player
        player = human_prediction    
    def game_play():
        # assigning the score for player and computer
        global player_score
        global computer_score
        global num_rounds    
        global winner 
        computer = random.choice(labels)
        print ('Computer choice is: ', computer)
        if player == 'nothing':
            print('Hand gesture not recognised, Please play again!')   
        if player == computer:
            print('Its a TIE!')     
        if player == 'rock':
            if computer == 'paper':
                print('You LOSE!')
                computer_score += 1
                num_rounds += 1
                print(f'Computer score is: ', computer_score)
                print(f'Number of rounds: ', num_rounds)
                print('Your current score is: ', player_score)   
            if computer == 'scissors':
                print('You WIN!')
                player_score += 1
                num_rounds += 1
                print(f'Computer score is: ', computer_score)
                print(f'Number of rounds: ', num_rounds)
                print('Your current score is: ', player_score)       
        elif player == 'paper':
            if computer == 'rock':
                print(computer, 'You WIN!')
                player_score += 1
                num_rounds += 1
                print(f'Computer score is: ', computer_score)
                print(f'Number of rounds: ', num_rounds)
                print('Your current score is: ', player_score)              
            if computer == 'scissors':
                print('You LOSE!')
                computer_score += 1
                num_rounds += 1
                print(f'Computer score is: ', computer_score)
                print(f'Number of rounds: ', num_rounds)
                print('Your current score is: ', player_score)
        elif player == 'scissors':
            if computer == 'paper':
                print('You WIN!')
                player_score += 1
                num_rounds += 1
                print(f'Computer score is: ', computer_score)
                print(f'Number of rounds: ', num_rounds)
                print('Your current score is: ', player_score)               
            if computer == 'rock':
                print('You Lose!')
                computer_score += 1
                num_rounds += 1
                print(f'Computer score is: ', computer_score)
                print(f'Number of rounds: ', num_rounds)
                print('Your current score is: ', player_score)
        if player_score or computer_score != 3:        
            print('Get ready to play again!!')
            time.sleep(3) 
        
    def game_winner(): 
        #diciding who the winner is by winning 3 games.   
        global winner     
        global num_rounds 
        global player_score
        global computer_score 
        if player_score == 3:
            winner = player  
            countdown = 5   
            for x in range(5):
                countdown -= 1
                print('Guessing who is the winner ...')
                time.sleep(5)
                print(f'Computer Picked: ',computer)   
                print('You are the WINNER!!')  
                
                play_again = input("Play again? (y/n): ")
                num_rounds = 0
                player_score = 0
                computer_score = 0
                if play_again != "y":
                    print("See you again ! BYE!!")                       
        if computer_score == 3:
            winner = computer    
            print('Guessing who is the winner...')
            time.sleep(5)
            print(f'Computer Picked: ',computer)
            print ('Computer is the WINNER!!')
            play_again = input("Play again? (y/n): ")
            num_rounds = 0
            player_score = 0
            computer_score = 0
            if play_again != "y":
                print("See you again ! BYE!!")
                
    def game_RPS():
        countdown()
        user_input()
        game_play()
        game_winner()
        
    
    game_RPS()
    