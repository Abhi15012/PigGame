# rolling the dice
import random

def roll():
    min_Value = 1
    max_Value = 6
    roll = random.randint(min_Value, max_Value)
    return roll

inputPlayers = int(input("Please enter the number of users playing the game (2-4)only:  "))

if inputPlayers <= 4 and inputPlayers >= 2:
    print("Number of players:", inputPlayers)
else:
    print("no entry")
    # import sys
    # sys.exit()

max_score = 50

player_scores = [0 for _ in range(inputPlayers)]

print("scores ",player_scores)

current_player = 0
for i in range(inputPlayers):
    while max(player_scores) < max_score:
        print(" ")
        print(f"player no:{i+1}")
        chance = input(f"Would you  like to roll (y/n): ")
        if chance.lower() == "y":
            Value = roll()
            if Value == 1:
                print("Opps! you rolled 1 .. Your score is 0.. better luck next time")
                player_scores[current_player] = 0
                current_player = (current_player + 1) % inputPlayers
                n = i + 1
                print(f" \n your scores are {player_scores}")
                break  # This will end the current player's turn

            else:
                player_scores[current_player] += int(Value)
                print(f"You have rolled {Value}")
                print(f"score of player:{i+1} is {player_scores[current_player]}")
        else:
            n = i + 1
            print(f"Now player no :{n+1} turn  \n All the best \n your scores are {player_scores}")
            current_player = (current_player + 1) % inputPlayers
            break  # This will end the current player's turn

    else:
         print(f"Congratulations {i+1}, you won the game \n your scores are {player_scores} \n \* game over\*")
         import sys
         sys.exit()
       