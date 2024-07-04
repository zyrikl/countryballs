# Countryballs battle simulator
# Created by Charles Wang

import random, time

player_alive = True
computer_alive = True

asia_names = ["China", "South Korea", "North Korea", "Japan", "India", "Indonesia", "Malaysia", "Mongolia", "Tibet", "Bhutan",
              "Philippines", "Taiwan", "Thailand", "Cambodia", "Laos", "Nepal"]
asia_health = ["2800", "1800", "600", "2500", "2600", "1000", "700", "600", "400", "400", "500", "1000", "900", "500", "300", "500"]
asia_damage = ["1000", "700", "900", "600", "700", "200", "200", "100", "100", "100", "200", "500", "400", "200", "400", "200"]
computer_id = random.randrange(0, len(asia_names))

player_ball = input("Your choice ball? ")
computer_ball = asia_names[computer_id]
computer_health = asia_health[computer_id]

# Compile into asia_names[?] format
for try_name in range(len(asia_names)):
    if player_ball == asia_names[try_name]:
        player_id = try_name

print("You are using "+asia_names[player_id]+", with "+asia_health[player_id]+" health.")
print("Your oppenent is using "+computer_ball+", with "+computer_health+" health.\n")

player_health = int(asia_health[player_id])

def turn(id_name, opponent_health):
    damage = random.randrange(1, int(asia_damage[id_name]))
    opponent_health = int(opponent_health) - damage
    return opponent_health

while (player_alive and computer_alive) == True:
    current_turn = turn(player_id, computer_health)
    time.sleep(random.randrange(1, 3))
    print(asia_names[player_id]+" just dealt "+str(int(computer_health) - int(current_turn))+
          " damage to your opponent, leaving them with "+str(current_turn)+" health left.")
    computer_damage = int(asia_damage[computer_id])
    computer_damage = random.randrange(1, computer_damage)
    computer_health = current_turn
    player_health = player_health - computer_damage
    time.sleep(random.randrange(1, 3))
    print(computer_ball+" just dealt "+str(computer_damage)+
          " damage to your opponent, leaving them with "+str(player_health)+" health left.\n")
    if computer_health <= 0:
        print("Opponent has died.")
        computer_alive = False
    if player_health <= 0:
        print("You have died.")
        player_alive = False
