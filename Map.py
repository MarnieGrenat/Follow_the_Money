class Map:
    '''
    Map class. It is responsible for loading the map from a file and transforming it into a matrix.
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
        Space Complexity: O(1)
        '''
        for i, row in enumerate(self.map):
            for j, element in enumerate(row):
                if element == "S":
                    return [i, j]


    def print_map_iteration(self, position: list) -> None:
        for i, row in enumerate(self.map):
            printed_row = row.copy()
            if i == position[0]:
                printed_row[position[1]] = self._VISITED
            print("".join(map(str, printed_row)))

    def get_initial_direction(self) -> list:
        '''
        Define the initial direction to follow in the map.
        '''
        return self.map[::][0].index(self._HORIZONTAL_STREET)

    def set_as__VISITED(self, row:int, column:int) -> None:
        '''
        Set the current position as _VISITED
        Time Complexity: O(1)
        Space Complexity: O(1)
        '''
        self.map[row][column] = self._VISITED

