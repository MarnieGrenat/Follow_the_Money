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

    def __init__(self, path: str) -> None:
        self.path = path
        self.map = self.__load_map()
        self.start = self.__find_start()

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

    def __find_start(self) -> list:
        '''
        Find the start position in the map
        Time Complexity: O(n)
        '''
        return self.map[::][0].index(self._HORIZONTAL_STREET)

    def print_map_iteration(self, position: list) -> None:
        '''
        Prints the map with the current position marked as visited.

        Args:
            position (list): The current position in the map.

        Returns:
            None
        '''
        for i, row in enumerate(self.map):
            printed_row = row.copy()
            if i == position[0]:
                printed_row[position[1]] = self._VISITED
            print("".join(map(str, printed_row)))

    def set_as_VISITED(self, row:int, column:int) -> None:
        '''
        Sets the current position as visited.

        Args:
            row (int): The row index of the current position.
            column (int): The column index of the current position.

        Returns:
            None
        '''
        self.map[row][column] = self._VISITED

