
import math
def minSideJumps(obstacles):
    res = 0
    lane = 2
    n = len(obstacles)
    i = 0
    while i < n-1: # recall that there is no obstacle in the final position, so it's safe to run only up to n-1
        if obstacles[i+1] == lane: # If the next obstacle is in our way
            res += 1 # we need to sidestep
            lanesCopy = [1,2,3] # This is how I chose to keep track of the lanes
            lanesCopy.remove(lane) # start w all lanes, remove the current one, now we have the others
            if obstacles[i] != 0: # If the current obstacle is not nothing, we can't jump somewhere
                if obstacles[i] == lanesCopy[0]: lane = lanesCopy[1]
                else: lane = lanesCopy[0]
            else: # both lanes are open
                for k in range(i+2, n+1): 
                    if k == n: return res # If we reach end of list without finding obstacles, done
                    if obstacles[k] == lane or obstacles[k] == 0: continue # we don't care about when there are no obstacles or when they are in the current lane
                    if obstacles[k] == lanesCopy[0]: lane = lanesCopy[1] # as soon as we find the next obstacle, we can move to the other lane
                    else: lane = lanesCopy[0]
                    i = k-2 # we don't technically need to do this, but this makes it O(N) guaranteed
                    break
        i += 1
    return res
# Read the number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    # Read the input for the current test case
    n = int(input())
    manholes = list(map(int, input().split()))

    # Find the minimum number of lane changes
    min_changes = minSideJumps(manholes)

    # Print the result for the current test case
    print(min_changes)
