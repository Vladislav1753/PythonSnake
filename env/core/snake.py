import numpy as np

from settings.constants import DIRECTIONS, SNAKE_BLOCK


class Snake:
    def __init__(self, head_position, direction_index, length):
        """
        @param head_position: tuple
        @param direction_index: int
        @param length: int
        """
        # Information snake need to know to make the move
        self.snake_block = SNAKE_BLOCK
        self.current_direction_index = direction_index
        # Alive identifier
        self.alive = True
        # Place the snake
        self.blocks = [head_position]
        current_position = np.array(head_position)
        for i in range(1, length):
            # Direction inverse of moving
            current_position = current_position - DIRECTIONS[self.current_direction_index]
            self.blocks.append(tuple(current_position))

    def step(self, action):
        # Execute one-time step within the environment
        """
        @param action: int
        @param return: tuple, tuple
        """
        # Check if action can be performed (do nothing if in the same direction or opposite)
        # Example: if snake looks left, pressing "left" or "right" buttons should change nothing
        if (action + 2) % 4 != self.current_direction_index:
            self.current_direction_index = action

            # Remove tail (can be implemented in 1 line)
        tail = self.blocks.pop()

        # Create new head
        new_head = (self.blocks[0][0] + DIRECTIONS[self.current_direction_index][0],
                    self.blocks[0][1] + DIRECTIONS[self.current_direction_index][1])


        # Add new head
        # Note: all Snake's coordinates should be tuples (X, Y)
        self.blocks = [new_head] + self.blocks

        return new_head, tail