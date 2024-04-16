class Atlas:
    '''
    Atlas class. It is responsible for loading the map from a file and transforming it into a matrix.

    Attributes:
        path (str)                                          :   The path to the map file.
        map (list)                                          :   The map represented as a matrix.
        start (list)                                        :   The starting position in the map.

    Methods:
        __init__(self, path: str) -> None                   :   Initializes a Map object.
        __load_map(self) -> list                            :   Loads the map from the file.
        __load_map_as_matrix(self, track:str) -> list       :   Transforms the map into a matrix.
        __find_start(self) -> list                          :   Finds the start position in the map.
        print_map_iteration(self, position: list) -> None   :   Prints the map with the current position marked as visited.
        set_as_VISITED(self, row:int, column:int) -> None   :   Sets the current position as visited.
    '''
    _VISITED             =   "X"
    _DEAD_END            =   "#"
    _WALL                =   "+"
    _VERTICAL_STREET     =   "|"
    _HORIZONTAL_STREET   =   "-"
    _CURVE               =   ['\\', '/']
    def __init__(self, path: str, debug:bool=False) -> None:
        self.path = path
        self.debug = debug

        self.map = self.__load_map()
        self.start = self.__find_start()

        self.last_pos = self.start
        self.map_copy = self.__load_map()
        for row in self.map_copy:
            for i in range(len(row)):
                if row[i] == self._WALL:
                    row[i] = ' '

    def __load_map(self) -> list:
        '''
        Load the map from the file
        Time Complexity: O(n)
        Space Complexity: O(n)
        '''
        with open(self.path, 'r') as file:
            map_file = file.read()

        # Make it usable for matrix iteration
        map_file = map_file.replace(' ', self._WALL)
        map_file = map_file[map_file.find('\n') + 1:]
        return self.__load_map_as_matrix(map_file)

    def __load_map_as_matrix(self, track:str) -> list:
        '''
        Transform the map into a matrix, where each element is a character of the map.
        Also add spaces to the end of each line to make the matrix a rectangle.
        Complexity: O(2n)
        Space Complexity: O(lines * columns)
        '''
        track  = track.split('\n')
        matrix = []
        for line in track:
            matrix.append(list(line))

        max_size = max(len(line) for line in matrix)
        for line in matrix:
            line.extend([self._WALL] * (max_size - len(line)))
        return matrix

    def __find_start(self) -> tuple:
        '''
        Find the start position in the map
        Time Complexity: O(n)
        '''
        for r in range(len(self.map[::][0])):
                if self.map[r][0] == self._HORIZONTAL_STREET:
                    if self.debug:
                        print(f"[VERBOSE] Start position: [{r}, 0]")
                    return [r, 0]

    def set_as_visited(self, pos:list) -> None:
        '''
        Sets the current position as visited.
        Args:
            row (int): The row index of the current position.
            column (int): The column index of the current position.
        Returns:
            None
        '''
        row, column = pos
        self.map[row][column] = self._VISITED

    '''
        DEBUG METHODS
    '''
    def print_map_iteration(self, position: list) -> None:
        '''
        Prints the map with the current position marked as visited.

        Args:
            position (list): The current position in the map.

        Returns:
            None
        '''
        for i, row in enumerate(self.map_copy):
            if i == position[0]:
                row[position[1]] = self._VISITED
            print("".join(self.map_copy(str, row)))

    def debug_control(self, pos:list) -> None:
        if self.debug:
            self.map_copy[self.last_pos[0]][self.last_pos[1]] = self._VISITED
            self.map_copy[pos[0]][pos[1]] = '@'
            self.last_pos = pos.copy()

    def debug_save(self, direction:dict) -> None:
        if self.debug:
            with open(self.path[:-4]+'_DEBUG.txt', 'w') as file:
                file.write(f"Last Direction: {direction}\n")
                for row in self.map_copy:
                    file.write("".join(map(str, row)) + '\n')
                file.close()