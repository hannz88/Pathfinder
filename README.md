# Pathfinder
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)

![Python Version](https://img.shields.io/badge/Python-3.7.4-brightgreen) 

A pathfinder algorithm that is based on breadth first search. It will plot the shortest route to the exit.


# Table of content

- [Running](#running)
- [File explanation](#file-explanation)
- [Usage](#usage)
- [Output](#output)
- [Algorithm Explanation](#algorithm-explanation)

# Running
[(Back to top)](#table-of-content)

The algorithm uses `Python 3.7.4`. So, make sure the `Python` installed is up to date. Then, run the following command on local terminal:
`python dungeon_escape_mk2.py`.

# File explanation
[(Back to top)](#table-of-content)

`dungeon_escape_mk1.py` is a simple pathfinder. It will only find a route to the exit. There is no guarantee that it is the shortest route. It will not tell you if it can't find an exit. It's simply a prototype.

`dungeon_escape_mk2.py` is the next version of pathfinder. It'll be able to finder the shortest route to the exit. If not, it'll raise an error.

`pathfinder.txt` shows an example of a simple maze.

`maze.txt` is another maze, albeit a bit more complicated.

# Usage
[(Back to top)](#table-of-content)

After running the file, it will ask for the path to the maze:
![Screenshot asking for path](https://github.com/hanz88/blob/master/Screenshots/pathname.png)

Please make sure that the file is in the `.txt` format. 

Here's an example of a maze that's included in `maze.txt`:
![Screenshot for maze](https://github.com/hanz88/blob/master/Screenshots/maze.png)

After the path name, it will print out your maze before proceeding to ask for the representation of:
- path
- wall
- entrance
- exit

# Output
[(Back to top)](#table-of-content)

After the necessary information are provided, the algorithm will output the following repeatedly:
- `last node`: The node the algorithm checked to see if it's viable.
- `Possible paths`: The viable paths up travelled so far.

Lastly, the shortest route will be shown. For example:
![Screenshot for output](https://github.com/hanz88/blob/master/Screenshots/output.png)
The shortest route is marked with `+`.
