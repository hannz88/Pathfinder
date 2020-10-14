# a Breadth-first search

# import libraries
import queue
from pprint import pprint

# create a maze
def createMaze2():
    maze = []
    maze.append(["#","#", "#", "#", "#", "O", "#", "#", "#"])
    maze.append(["#"," ", " ", " ", " ", " ", " ", " ", "#"])
    maze.append(["#"," ", "#", "#", " ", "#", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", " ", " ", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", "#", " ", "#", "#", "#"])
    maze.append(["#"," ", " ", " ", " ", " ", " ", "#", "#"])
    maze.append(["#","#", "#", "#", "#", "#", " ", "X", "#"])
    return maze

# take in user's path for the dungeon
def create_maze_from_path(pathname):
    """
    Takes in the path name and output the dungeon as list.
    """
    dungeon = []
    with open(pathname) as f:
        for line in f:
            print(line)
            dungeon.append([char for char in line.rstrip()])
    return dungeon

# create a class call Node
class Node():
    def __init__(self, symbol, coord):
        self.symbol = symbol  # referring to the symbol used in the maze
        self.coord = coord  # the position
        self.visited = False  # ie each node is not visited yet
        
    def __repr__(self):
        return repr(self.coord)

# create a class in order to print the content of the queue
class PrintableQueue(queue.Queue):
    def __str__(self):
        return(str(list(self.queue)))
    
    def __repr__(self):
        return(f"PrintableQueue({self.__str__()})")
        
# create a class to handle error
class NoEscape(Exception):
    pass
    
# to transform a maze into Node object
def translate_to_node(input_maze, path: str, wall: str, exit: str, entrance: str):
    """
    Transform the text-based maze into Node objects.
    Path is the usable path
    Put in the symbols used in maze with "" around it.
    """
    translate = {path:'o', wall:'x', exit:'g', entrance:'S'}
    dungeon = []
    for i, row in enumerate(input_maze):
        tmp_row = []
        for j, symbol in enumerate(row):
            tmp = Node(translate[symbol], (i, j))
            tmp_row.append(tmp)
        dungeon.append(tmp_row)
    return dungeon

# get the starting coord as Node
def get_node_s(dungeon):
    """
    dungeon at this point is already a Node object.
    get the start coordinate of the dungeon as a Node object.
    """
    for item in dungeon:
        for val in item:
            if val.symbol == "S":
                return val
    return False

def breadth_first_search(dungeon, start):
    """
    Both the dungeon and start are Node objects.
    Find the shortest path
    """
    travels = PrintableQueue()  # keep track of all the paths travelled
    route = []
    route.append(start)
    travels.put(route)
    
    # if the start is already the exit
    if start.symbol == 'g':
        return route.get()
    
    # otherwise
    start.visited = True
    width = len(dungeon[0])
    height = len(dungeon)
    
    # all possible moves
    moves = {"U":(-1,0), 
         "D":(1,0), 
         "R":(0,1), 
         "L":(0,-1)}
    
    # loop through all moves while the travels is not empty

    while travels:
        print(travels)
        path = travels.get()
#         print(f"itt: {itt} - path:{path}")
        
        last_node = path[-1]
        print(f"last_node:{last_node.coord}")
#         print(f"itt: {itt} - last_node:{last_node}")
        coord = last_node.coord
#         itt+=1
        for direction in moves:
#             print(f"direction:{direction}")
#             print(f"coord[0]:{coord[0]}")
            new_x = coord[0] + moves[direction][0]
            new_y = coord[1] + moves[direction][1]
            if (new_x < 0 or new_x >= height) or (new_y < 0 or new_y>=width):  # if the new moves fell outside of the boundary
                continue
            new_node = dungeon[new_x][new_y]
#             print(f"new_node:{new_node}")
            if new_node.symbol == "g":  # if the new_node is the exit
                return path + [new_node]
            elif new_node.symbol == 'o' and new_node.visited == False:  # if the new_node hadn't been visited and is an empty path
                new_node.visited = True
                new_path = path.copy()
                new_path.append(new_node)
                travels.put(new_path)
                
    raise NoEscape('There\'s no exit!')

# to trace solution
def trace_path(maze, solution):
    """
    maze is not Node object.
    Solution is a list of tuples indicating the path/ nodes taken.
    """
    maze_copy = maze.copy()
    for step in solution[1:len(solution)-1]:
        coord = step.coord
        i = coord[0]
        j = coord[1]
        maze_copy[i][j] = "+"
    return maze_copy

if __name__ == "__main__":
    filepath = input("Please provide the full path to you maze:")
    mazetxt = create_maze_from_path(filepath)
    path = input("Please provide the symbol for usable path. If empty please press space:")
    wall = input("Please provide the symbol for wall:")
    entrance = input("Please provide the symbol for entrance:")
    exit = input("Please provide the symbol for exit:")
    dungeon_node = translate_to_node(mazetxt, path, wall, exit, entrance)
    start = get_node_s(dungeon_node)
    try:
        solution = breadth_first_search(dungeon_node, start)
        pprint(trace_path(mazetxt, solution))
    except NoEscape as e:
        print(e)
