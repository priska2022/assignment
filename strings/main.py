# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
# Finale UEFA Euro 1988
# part 1
# Create a variable for each player who scored

player_0 = "Ruud Gullit"
player_1 = "Marco van Basten"

# Create a variable for each minute of the game in which a goal was scored
goal_0 = 32
goal_1 = 54

# Using the +-operator, create a string that reports on who scored when

scorers = player_0 + " " + str(goal_0) + " " + player_1 + " " + str(goal_1)

# Use f-strings or the +-operator to create a single string with information about who scored when

report = f"{player_0} scored in the {goal_0}nd minute \n{player_1} scored in the {goal_1}th minute "
#print(report)

# part 2
# Choose a player that played in the soccer match and store his name as a string

player = 'Marco van Basten'
first_name = player[0:5]
player.find('Marco')
#print(first_name)


player.find('van Basten')
last_name= player[6:]
#print(last_name)

last_name_len = len(last_name)
#print(last_name_len)

name_short = 'M. van Basten'

chant = 'Marco!' * 5
#print(chant)

good_chant = chant != 5
#print(good_chant)



