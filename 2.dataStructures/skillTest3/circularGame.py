def findWinner(n, k):
    friends = list(range(1, n + 1))  # Initialize the list of friends

    current_index = 0  # Start at the 1st friend
    while len(friends) > 1:
        # Count k friends in the clockwise direction
        next_index = (current_index + k - 1) % len(friends)
        # Remove the last counted friend from the circle
        friends.pop(next_index)
        # Update the current index for the next iteration
        current_index = next_index

    # Return the winner (last friend remaining in the circle)
    return friends[0]

# Taking input
n, k = map(int, input().split())

# Finding the winner
winner = findWinner(n, k)
print(winner)
