# Pathfinder
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)

![Python Version](https://img.shields.io/badge/Python-3.7.4-brightgreen) 

A collection of algorithms that I wrote showcasing different algorithms to find the route through a maze.


# Table of content

- [Running](#running)
- [File explanation](#file-explanation)
- [Usage](#usage)
- [Output](#output)
- [Algorithm Explanation](#algorithm-explanation)
- [Links](#links)

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

![Screenshot asking for path](https://github.com/hannz88/Pathfinder/blob/master/Screenshots/pathname.png)

Please make sure that the file is in the `.txt` format. 

Here's an example of a maze that's included in `maze.txt`:

![Screenshot for maze](https://github.com/hannz88/Pathfinder/blob/master/Screenshots/maze.png)

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

![Screenshot for output](https://github.com/hannz88/Pathfinder/blob/master/Screenshots/output.png)

The shortest route is marked with `+`.

# Algorithm Explanation
Here is the explanation for the idea behind `dungeon_escape_mk2.py`. The code is based on the Breadth First Search algorithm. The idea is that the algorithm will explore all routes, one node at a time. The first one to reach the exit will then be the shortest route. In other words: start at the root/ entrance, then explore the neighbours before moving onto the children of the neighbours. The pseudocode is as follows:

```
1. Start at the root/ entrance.
2. Place the root/ entrance into the a queue, Travels.
3. While Travels is not empty:
    1. Remove the current path from Travels.
    2. Get the last visited node from Travels. For every child of the node:
        1. If it's exit, return the child with the current path.
        2. If not exit and if it's a viable path:
            1. Mark the child node as visited and append the child node to the current path.
            2. Place the newly appended current path to Travels
```

# Links
* [Path Finding Algorithms](https://medium.com/omarelgabrys-blog/path-finding-algorithms-f65a8902eb40)
* [Breadth First Search Wikipedia](https://en.wikipedia.org/wiki/Breadth-first_search)
