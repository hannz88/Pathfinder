import pprint
dungeon = []

# a Greedy pathfinder
# does not have a way to print if there are no exit
with open("/home/han/Projects/Hackerrank/pathfinder.txt") as file:
    for line in file:
        print(line)
        dungeon.append(line.rstrip())

# find the location of s first
def get_s(los):
    """
    los = list of strings
    get the index of the string within the list where s is at.
    Get the index of s in the string.
    """
    for i in range(len(los)):
        if "s" in los[i]:
            s_x = i
            s_y = los[i].index("s")
    return s_x, s_y

# create a function that just look
# the function will return true if the direction it looks contain a path
def look(x,y,direction):
    """
    x is the row
    y is the column
    direction is U,R,D,L
    """
    acceptable_path = [".", 'E']
    if (x==0) and (direction=="U"):
        return False
    if (y==len(dungeon[0])) and (direction=="R"):
        return False
    if (x==len(dungeon)-1) and (direction=="D"):
        return False
    if (y==0) and (direction=="L"):
        return False
    if direction=="U":
        if dungeon[x-1][y] in acceptable_path:
            return True
        return False
    if direction=="D":
        if dungeon[x+1][y] in acceptable_path:
            return True
        return False
    if direction == "R":
        if dungeon[x][y+1] in acceptable_path:
            return True
        return False
    if direction == "L":
        if dungeon[x][y-1] in acceptable_path:
            return True
        return False
    
prev_direction = ""  # to prevent it from coming back the same way it did
def move(x,y):
    """
    Takes two coordinates and move in the direction where there's a path by one step.
    """
    move_list = ["U", "R", "D", "L"]
    opposites = {
        "U": "D", 
        "D":"U", 
        "R":"L", 
        "L":"R"
    }
    global prev_direction
    for direction in move_list:
        print(direction)
        if opposites[direction] == prev_direction:
            continue
        ispath = look(x,y,direction)
        print(f"ispath: {ispath}")
        if ispath == True:
            if direction == "U":
                x -= 1
            elif direction == "R":
                y += 1
            elif direction == "D":
                x += 1
            elif direction == "L":
                y -= 1
#             if (x==moves[-1][0]) and (y==moves[-1][1]):
#                 continue
            break
#         elif (direction=="L") and (ispath == False): 
#             return False
    prev_direction = direction
    return x,y

if __name__ == "__main__":
    moves = []
    start = get_s(dungeon)
    x = start[0]
    y = start[1]
    moves.append(start)
    while dungeon[x][y] != "E":
        next_step = move(x,y)
        moves.append(next_step)
        x = next_step[0]
        y = next_step[1]
    

