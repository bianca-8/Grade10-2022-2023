def directionConverter(direction):
  if direction == 1:
    word = "positive y"
  elif direction == 2:
    word = "negative x"
  elif direction == 3:
    word = "negative y"
  elif direction == 4:
    word = "positive x"
  return word 

x = 0
y = 0

command = ""
direction = 1

# down: 1
# left: 2
# up: 3
# right: 4

command = input("Please enter your command: ").lower()

if command == "start":
  while command != "stop": 
    print("\n\nThe rover is currently at position (%i, %i)." %(x,y))
    print("The rover is currently facing the %s direction." %directionConverter(direction))
    
    command = input("\nPlease enter your command: ").lower()
    
    if command == "right":
      direction += 1
      if direction == 5:
        direction = 1
        
    elif command == "left":
      direction -= 1
      if direction == 0:
        direction = 4
        
    if "forward" in command:
      if command[-1].isdigit() == True:
        space = command.find(" ")
        n = command [space + 1:]
        n = int(n)
        
      else: 
        n = 1
        
      if direction == 1:
        y += n
      
      elif direction == 2:
        x -= n
        
      elif direction == 3:
        y -=n
        
      else:
        x += n
