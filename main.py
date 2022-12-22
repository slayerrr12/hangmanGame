import random


# the game engine code
def game(game_word,flag,guessing_variable) :
    
    actual_word = list(game_word)
    play_again = 'y'
    flag2 = 0
     
    
    
       
    while True :
            if flag == 0 :
                print(" The Poor Hangman was killed!! :(")
                play_again = input("Wanna play again?...if yes enter y.... if no enter n : ")
                break 
                
                
            
            elif flag == 100 :
                print ("You saved the hangman from dying!!!!")
                
                play_again = input("Wanna play again?...if yes enter y.... if no enter n : ")
                break
                
                
            else :
                
                print(guessing_variable)
                k = input("Your alphabet : ")
                
                
                for i in range(len(game_word)) :
                    if game_word[i] == k :
                        game_word[i] = '0'
                        guessing_variable[i] = k
                        flag2+=1
                if flag2 == 0 :
                     print("WRONG GUESS!!!!!")
                     print(f"{flag} steps away from dying")
                     flag-=1
                     print(guessing_variable)
                if flag2 != 0 :
                     print(guessing_variable)
                     flag2 = 0
            if actual_word == guessing_variable :
                flag = 100
                
    return play_again
                     

# test if user has on won the game
def test_if_complete(word1,word2):
    if word1 == word2 :
        return True
    else :
        return False





redux = ["list","block","guy","dude","random","jigsaw","blessed","upbringer"]
test_word = ""



# random word generator
test_word = redux[random.randint(0, len(redux)-1)]


# storing the string as a list
game_word = list(test_word)
guessing_variable = []
# intialising all elements as 0 in our string
for i in range(len(game_word)) :
    guessing_variable.append('0')
      

print("THIS IS YOUR HANGMAN GAME\n\n\n\n\n\n\n")

print(guessing_variable)
print("guess the word:")
flag = 6
play_again = 'y'

while play_again == 'y' :
    play_again = game(game_word,flag,guessing_variable)
    test_word = redux[random.randint(0, len(redux)-1)]
    game_word = list(test_word)
    guessing_variable = []
    for i in range(len(game_word)) :
        guessing_variable.append('0')


#--------------------------------------------------------------changes to be made---------------------------------------------------------

#write the word if the user does'nt win the game
#add an back track process for user



                     



    
    









