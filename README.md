So this is my project that generates the maze using recursive backtracker of my own creation. I'm also working on algorithm which will find the shortest way from beginning to the end but it's not finished yet so please don't mind the solve_maze function and if you want to test the generation algorithm simply don't call the solve_maze.
Even though the solving algorithm is not finished yet I will tell about it's theory but for understanding it you have to know how the maze creation works, so please check it out first.
1. While we create the maze we want to get hold of the information about how the algorithm reached every cell, f.e. it reached the cell on coordinates (x, y) by going left.
2. Using this information we want the algorithm to analyze every cell in the maze and figure out the available ways of getting out of every cell so the algorithm knows whetehr there is a wall in front of him or not.
3. We already have a information about how we can get out of every cell, the algorithm acquired this information in step one. So, f.e. for a given cell if we got to it by going left we can get out by going right, right :)
4. But what about any other possible ways of going out? Well for them we have to know how the algorithm reached the cell above, on right, below and on left. Now if the cell above was reached by going up then there is no wall in front of us and the algorith is free to go, same for cell on right which if it was reached by going right means thath it can be accessed and so on for the two cells left.
5. Now when we know every cell's ways to get out of it, we must eliminate dead ends which are cell that only one direction lets us to leave.
6. Then we have to know the location of every cell which has 3 or more ways out of.
7. Now when we have all of the information, here is a pseudocode for the solving operation:

```
for cell in all_cells:
  if cell == multiple_ways_cell:
    analyse every possible direction:
      if you reach dead end eliminate this direction
      elif you reach other multiple_ways_cell:
        mark this direction as a correct way
```   
