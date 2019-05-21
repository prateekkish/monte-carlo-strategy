import random

def switching_player():
  doors = [1,2,3]
  car_behind_door = random.choice(doors)
  player_first_choice = random.choice(doors)
  
  if car_behind_door != player_first_choice:
    # get the door which will be eliminated by the show host
    doors_to_eliminate_by_host = doors.copy()
    doors_to_eliminate_by_host.remove(player_first_choice) # cannot eliminate player's choice
    doors_to_eliminate_by_host.remove(car_behind_door) # cannot eliminate the door with car

    doors.remove(player_first_choice) # since player will switch, cannot stay at original choice
    doors.remove(doors_to_eliminate_by_host[0]) # cannot choose the eliminated door
    player_second_choice = doors[0] # player chooses the last remaining door

    return 1 if player_second_choice == car_behind_door else 0

  else:
    # if player choose the car door in first go, switching will result in loss for sure
    return 0

def non_switching_player():
  doors = [1,2,3]
  car_behind_door = random.choice(doors)
  player_choice = random.choice(doors)

  return 1 if player_choice == car_behind_door else 0

trials = 100000
switching_result = 0
non_switching_result = 0
for i in range(trials):
  switching_result += switching_player()
  non_switching_result += non_switching_player()

print(f"By switching, out of {trials} attempts, I won {switching_result} times")
print(f"By not switching, out of {trials} attempts, I won {non_switching_result} times")


