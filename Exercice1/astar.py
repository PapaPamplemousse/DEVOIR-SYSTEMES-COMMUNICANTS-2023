# /*
#  * /FILE
#  * 	astar.py
#  * 
#  * /AUTHOR
#  *      REIF Hugo       <hugo.reif.faudemer@gmail.com>  || <21701260@etu.unicaen.fr>
#  *      
#  * /DESCRIPTION 
#  *      Astar in the case of planning for moving 3 robots
#  * 
#  * /DATES
#  *      24/11/2022 : Original Code
#  */

from heapq import heappush, heappop

def find_joint_plan(grid, start_positions, end_positions):
  # Initialize the frontier with the starting state
  frontier = []
  heappush(frontier, (0, start_positions))

  # Initialize dictionaries to record movements and costs
  came_from = {tuple(start_positions): None}
  cost_so_far = {tuple(start_positions): 0}

  # Iterate until a plan is found or all states have been explored
  while frontier:
    # Retrieve the current state (with the minimum cost) from the frontier
    current_cost, current_positions = heappop(frontier)

    # Check if the current state is the final state, in which case we have found a plan
    if current_positions == end_positions:
      break

    # Explore all possible actions for each robot
    for i in range(3):
      for action in actions:
        # Calculate the new position of the robot after the action
        new_x, new_y = current_positions[i]
        if action == "up":
          new_x -= 1
        elif action == "down":
          new_x += 1
        elif action == "left":
          new_y -= 1
        elif action == "right":
          new_y += 1

        # Check that the new position is valid (on the grid and not occupied by another robot)
        if new_x < 0 or new_x >= len(grid) or new_y < 0 or new_y >= len(grid[0]) or (new_x, new_y) in current_positions[:i] + current_positions[i+1:]:
          continue
        new_positions = current_positions[:i] + [(new_x, new_y)] + current_positions[i+1:]


        #  Calculate the cost of the action (using Manhattan distance as the heuristic function)
        cost = cost_so_far[tuple(current_positions)] + abs(new_x - end_positions[i][0]) + abs(new_y - end_positions[i][1])


        #cost = cost_so_far[current_positions] + abs(new_x - end_positions[i][0]) + abs(new_y - end_positions[i][1])
        if tuple(new_positions) not in cost_so_far or cost < cost_so_far[tuple(new_positions)]:
          cost_so_far[tuple(new_positions)] = cost

          priority = cost + sum(abs(new_x - end_positions[i][0]) + abs(new_y - end_positions[i][1]) for i in range(3))
          heappush(frontier, (priority, new_positions))
          came_from[tuple(new_positions)] = current_positions

# Build the plan from the movements recorded in came_from
  plan = []
  current = end_positions
  while current != start_positions:
    plan.append(current)
    current = came_from[tuple(current)]
  #Add the starting position to the plan
  plan.append(start_positions)
  plan.reverse()
  return plan


def visualize_plan(grid, plan):
  for positions in plan:
    for i in range(3):
      x, y = positions[i]
      grid[x][y] = i+1
    print_grid(grid)
    print ("\n")

def print_grid(grid):
  for row in grid:
    print(" ".join(str(cell) if cell != 0 else "." for cell in row))

# Example usage: 

# List of possible actions for each robot
actions = ["up", "down", "left", "right"]

# Grid example
grid = [  [0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0],
]

# Starting positions for each robot
start_positions = [(0, 0), (3, 0), (3, 1)]
#Ending positions for each robot
end_positions = [(5, 2), (1, 4), (0, 4)]
# Find the joint plan
plan = find_joint_plan(grid, start_positions, end_positions)
# Visualize the plan
visualize_plan(grid, plan)
