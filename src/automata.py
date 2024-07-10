class ElementaryAutomata:
    DEAD_STATE = 0
    ALIVE_STATE = 1

    def __init__(self, size: int, rule: int, boundary_condition: str):
        """
        Initializes the Elementary Automata.

        :param size: Number of cells in the grid.
        :param rule: Rule number (0-255).
        :param boundary_condition: ('fixed_dead', 'fixed_alive', 'periodic', 'adiabatic', 'reflexive').
        """
        self.size = size
        self.rule = self._parse_rule(rule)
        self.boundary_condition = boundary_condition

        self._grid = self._initialize_grid()
        self._left_boundary, self._right_boundary = self._apply_boundary_condition()

    def _initialize_grid(self) -> list:
        """
        Initializes the grid with a single live cell in the center.

        :return: The initial state of the grid.
        """
        grid = [self.DEAD_STATE] * self.size
        grid[self.size // 2] = self.ALIVE_STATE
        return grid

    @staticmethod
    def _parse_rule(rule) -> str:
        """
        Parses the rule number to binary representation.

        :param rule: Rule number (0-255)
        :return: The binary representation of the rule.
        """
        return bin(rule)[2:].zfill(8)

    def _apply_boundary_condition(self) -> tuple:
        """
        Applies the boundary condition to the grid.

        :return: The states of the left and right boundary.
        :raises ValueError: If an invalid boundary condition is provided.
        """
        if self.boundary_condition == 'fixed_dead':
            left_boundary = self.DEAD_STATE
            right_boundary = self.DEAD_STATE
        elif self.boundary_condition == 'fixed_alive':
            left_boundary = self.ALIVE_STATE
            right_boundary = self.DEAD_STATE
        elif self.boundary_condition == 'periodic':
            left_boundary = self._grid[-1]
            right_boundary = self._grid[0]
        elif self.boundary_condition == 'adiabatic':
            left_boundary = self._grid[0]
            right_boundary = self._grid[-1]
        elif self.boundary_condition == 'reflexive':
            left_boundary = self._grid[1]
            right_boundary = self._grid[-2]
        else:
            raise ValueError(f'Invalid boundary condition: "{self.boundary_condition}"')

        return left_boundary, right_boundary

    def _get_neighborhood(self, idx: int) -> int:
        """
        Returns the neighborhood of a cell, accounting for boundary conditions.

        :param idx: The index of the current cell.
        :return: The integer representation of the neighborhood
        """
        left_neighbor = self._grid[idx - 1] if idx - 1 >= 0 else self._left_boundary
        right_neighbor = self._grid[idx + 1] if idx + 1 < self.size else self._right_boundary
        center = self._grid[idx]
        return int(f'{left_neighbor}{center}{right_neighbor}', 2)

    def evolve(self) -> list:
        """
        Evolves the automaton to the next generation and returns a copy of the grid.

        :return: The 1D grid of cellular automata
        """
        temp_grid = self._grid[:]

        for idx in range(self.size):
            neighborhood = self._get_neighborhood(idx)
            temp_grid[idx] = int(self.rule[7 - neighborhood], 2)

        self._grid = temp_grid[:]
        self._left_boundary, self._right_boundary = self._apply_boundary_condition()

        return self._grid[:]

    def __str__(self) -> str:
        """
        Returns a string representation of the current state of the grid.

        :return: The string representation of the grid.
        """
        left_str = '□┋ ' if self._left_boundary == self.DEAD_STATE else '■┋ '
        right_str = ' ┋□' if self._right_boundary == self.DEAD_STATE else ' ┋■'
        grid_str = ''.join(['□' if cell == self.DEAD_STATE else '■' for cell in self._grid])

        return f"{left_str}{grid_str}{right_str}"