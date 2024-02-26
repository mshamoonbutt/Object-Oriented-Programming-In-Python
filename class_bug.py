class Bug:
    def __init__(self, initial_position):
        """Initialize the Bug with an initial position."""
        self.position = initial_position
        self.direction = 1  # 1 represents moving to the right, -1 represents moving to the left

    def turn(self):
        """Change the direction of the Bug."""
        self.direction *= -1

    def move(self):
        """Move the Bug one unit in the current direction."""
        self.position += self.direction

    def getPosition(self):
        """Get the current position of the Bug."""
        return self.position

# Sample usage:
bugsy = Bug(10)

# Initial position
print("Initial Position:", bugsy.getPosition())

# Move and turn
bugsy.move()
print("After Move:", bugsy.getPosition())
bugsy.turn()
bugsy.move()
print("After Turn and Move:", bugsy.getPosition())
