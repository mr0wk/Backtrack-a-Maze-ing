This is my project that generates the maze using recursive backtracker of my own creation. I'm also working on the algorithm which aim is to find the shortest way but it's not finished yet so please comment out the 'solve_maze' function if you want to test the generation algorithm.

Even though the solving algorithm is not finished yet I've develepoed it's theory using pseudo code, but in order to understanding it you have to know how the maze creation algorithm works, so please test the code and then you can read about the solving algorithm's instructions and it's pseudo code.


Solving algorithm's instructions:

1. While we create the maze we want to get hold of the information about how the algorithm reached every cell, f.e. it reached the cell on coordinates (x, y) by going left.

2. Using this information we want the algorithm to analyze every cell in the maze and figure out the available ways of getting out of every cell so that the algorithm knows whether there's a 'wall' in front of him or not.

3. We already have an information about how we can get out of every cell, the algorithm acquired it in step one, so f.e. for a given cell if we got to it by going left, naturally we can get out of it by going right, right? :)

4. But what about any other possible ways of getting out? Well for the algorithm to figure them out we have to know how it reached the cell above, on right, below and on left. Now if the cell above was reached by going up then the algorith knows that there is no wall, same for the cell on right which if reached by going right can be accessed by going right and so on for the other cells.

5. Now when we know every cell's ways out, we must eliminate dead ends which are cells that only have a one way of getting out.

6. Then we have to know the location of every cell which has 3 or more ways out of it, these are some sort of crossroads and every road has to be visited by the algorithm.

7. The goal for the algorithm is to move from one crossroad to another and eventually eliminate all of the roads that lead the algorithm to dead ends resulting in finding a shortest way to solve the maze/

Pseudo code:

```
eliminate_dead_ends()
for cell in all_cells:
  if cell == dead_end:
        go back to the latest crossroad and don't go this way again
  elif cell == multiple_ways_cell:
    analyse_every_possible_direction():
      if cell == dead_end:
        go back to the latest crossroad and don't go this way again
      elif you reach other crossroad:
        mark this crossroad as latest crossroad
        analyse_every_possible_direction()
```   
