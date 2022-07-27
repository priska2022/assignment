# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
# Finale UEFA Euro 1988

# # part 1
# Create a variable for each player who scored
player_0 = "Ruud Gullit"
player_1 = "Marco van Basten"

# Create a variable for each minute of the game in which a goal was scored
goal_0 = 32
goal_1 = 54

# Using the +-operator, create a string that reports on who scored when

scorers = player_0 + " " + str(goal_0) + ", " + player_1 + " "+ str(goal_1)
print(scorers)

# Use f-strings or the +-operator to create a single string with information about who scored when

report = f"{player_0} scored in the {goal_0}nd minute\n{player_1} scored in the {goal_1}th minute"
print(report)

# part 2
# Choose a player that played in the soccer match and store his name as a string

player = 'Marco van Basten'

#use slicing and the find-method to isolate the player's first name
first_name = player[:player.find(' ')]
#print(first_name)
#print(player.find(' '))
#print(player[:player.find(' ')])

#use find methode, slicing and len to isolate the player's last name
last_name_len = len(player[player.find(' ')+1 :])
print(last_name_len)

name_short = player[:1] + '.' + player[player.find(' '):]
print(name_short)

chant = ((first_name + '! ') * len(first_name)).strip()
print(chant)

good_chant = chant[-1:] != ' '
print(good_chant)



